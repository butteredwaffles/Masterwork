import json
import subprocess
import tempfile
from typing import Any, Dict, List, Union, Optional
from pathlib import Path
from enum import IntEnum

from core import resources
from core.save.potionomics_save import *


def _clean_property_name(name: str) -> str:
    """
    Clean property names by removing trailing indices.
    Example: "CardLibrary_0" -> "CardLibrary"
    Also handles mangled property names from UE4.
    """
    import re
    # Remove trailing _N pattern where N is a digit
    cleaned = re.sub(r'_\d+$', '', name)
    return cleaned

def _extract_property_value(prop_data: Any) -> Any:
    """
    Extract the actual value from a property, recursively unwrapping nested structures.
    Handles all UE4 property types: primitives, arrays, structs, maps, etc.
    """
    if not isinstance(prop_data, dict):
        return prop_data

    # Direct value types
    if "Int" in prop_data:
        return prop_data["Int"]
    elif "Float" in prop_data:
        return prop_data["Float"]
    elif "Double" in prop_data:
        return prop_data["Double"]
    elif "Bool" in prop_data:
        return prop_data["Bool"]
    elif "Name" in prop_data:
        return prop_data["Name"]
    elif "Str" in prop_data:
        return prop_data["Str"]
    elif "Object" in prop_data:
        return prop_data["Object"]
    elif "Int8" in prop_data:
        return prop_data["Int8"]
    elif "Int16" in prop_data:
        return prop_data["Int16"]
    elif "Int64" in prop_data:
        return prop_data["Int64"]
    elif "UInt8" in prop_data:
        return prop_data["UInt8"]
    elif "UInt16" in prop_data:
        return prop_data["UInt16"]
    elif "UInt32" in prop_data:
        return prop_data["UInt32"]
    elif "UInt64" in prop_data:
        return prop_data["UInt64"]

    # Text type - return the Text dict itself to preserve structure for localization
    elif "Text" in prop_data:
        return prop_data["Text"]

    # Enum type
    elif "Enum" in prop_data:
        enum_val = prop_data["Enum"]
        # Extract just the enum value name (e.g., "ETutorials::NewEnumerator6" -> "NewEnumerator6")
        if isinstance(enum_val, str) and "::" in enum_val:
            return enum_val.split("::")[-1]
        return enum_val

    # Byte enum type
    elif "Byte" in prop_data:
        byte_val = prop_data["Byte"]
        if isinstance(byte_val, dict) and "Label" in byte_val:
            label = byte_val["Label"]
            if isinstance(label, str) and "::" in label:
                return label.split("::")[-1]
            return label
        return byte_val

    # Array type
    elif "Array" in prop_data:
        arr_data = prop_data["Array"]
        if isinstance(arr_data, dict):
            # Base types array
            if "Base" in arr_data:
                base = arr_data["Base"]
                if isinstance(base, dict):
                    # Extract the array from the first (and only) key
                    for values in base.values():
                        if isinstance(values, list):
                            # Recursively extract each element
                            return [_extract_property_value(v) if isinstance(v, dict) else v for v in values]
                        return values
                return base
            # Struct array
            elif "Struct" in arr_data:
                struct_array = arr_data["Struct"]
                if "value" in struct_array:
                    return [_extract_struct(s) for s in struct_array["value"]]
                return []
        return arr_data

    # Struct type
    elif "Struct" in prop_data:
        return _extract_struct(prop_data["Struct"])

    # Map type
    elif "Map" in prop_data:
        map_data = prop_data["Map"]
        result = {}
        if isinstance(map_data, list):
            for entry in map_data:
                if isinstance(entry, dict) and "key" in entry and "value" in entry:
                    key = _extract_property_value(entry["key"])
                    value = _extract_property_value(entry["value"])
                    # Use string key for dict
                    result[str(key)] = value
        return result

    # SoftObject
    elif "SoftObject" in prop_data:
        return prop_data["SoftObject"]

    # FieldPath
    elif "FieldPath" in prop_data:
        return prop_data["FieldPath"]

    # Default: return as-is
    return prop_data


def _extract_struct(struct_data: Any) -> Dict[str, Any]:
    """
    Extract values from a struct, recursively handling nested structures.
    """
    if not isinstance(struct_data, dict):
        return struct_data

    # Check if it has nested "Struct" key (indicating properties)
    if "Struct" in struct_data:
        props = struct_data["Struct"]
        if isinstance(props, dict):
            result = {}
            for key, value in props.items():
                result[_clean_property_name(key)] = _extract_property_value(value)
            return result

    # Direct properties
    result = {}
    for key, value in struct_data.items():
        if key != "tag":  # Skip schema/tag information
            result[_clean_property_name(key)] = _extract_property_value(value)
    return result


def _load_from_json(json_data: Union[str, Dict[str, Any], Path]) -> Dict[str, Any]:
    """Load save data from JSON format (from uesave-rs)."""
    if isinstance(json_data, (str, Path)):
        if isinstance(json_data, str) and (json_data.startswith('{') or json_data.startswith('[')):
            data = json.loads(json_data)
        else:
            with open(json_data, 'r') as f:
                data = json.load(f)
    else:
        data = json_data

    if "root" not in data or "properties" not in data["root"]:
        raise ValueError("Invalid save data format: missing root.properties")

    properties = data["root"]["properties"]
    result = {}

    # Parse all properties
    for prop_name, prop_data in properties.items():
        clean_name = _clean_property_name(prop_name)
        result[clean_name] = _extract_property_value(prop_data)

    return result

class PotionomicsUESaveParser(PotionomicsSave):
    def _convert_enum_string(self, enum_string: str, enum_class) -> Optional[object]:
        """Convert UE4 enum string to Python Enum instance."""
        if not enum_string:
            return None
        
        # Strip the "EEnumName::" prefix if present
        if '::' in enum_string:
            enum_string = enum_string.split('::')[-1]
        
        try:
            return enum_class(enum_string)
        except (ValueError, KeyError):
            return None
    
    def _extract_text_name(self, name_data) -> str:
        """Extract name from Text property or string."""
        if isinstance(name_data, dict):
            variant = name_data['variant']
            if 'StringTableEntry' in variant:
                return variant['StringTableEntry']['key']
            else:
                return ''
        elif isinstance(name_data, str):
            return name_data
        return ''
    
    def get_flags(self) -> dict[str, bool]:
        return self.raw_parsed.get('Flags')

    def get_active_chapter(self) -> int:
        return self.raw_parsed.get('ActiveChapter')

    def get_daily_stats(self) -> List[DailyStats]:
        return [DailyStats(money_earned=stat['GoldEarned'], money_spent=stat['GoldSpent'], number_of_customers=stat['NumberOfCustomers'], potions_sold=stat['PotionsSold']) for stat in self.raw_parsed.get('DailyStats', [])]

    def get_relationships(self) -> dict[str, Relationship]:
        return {k: Relationship(num_coupons=len(v['CouponDataKeys']), flirt_points=v['FlirtPoints'], hangout_level=v['HangoutLevel'], level=v['Level'], value=v['Value']) for k, v in self.raw_parsed.get('Relationships', {}).items()}

    trait_map = {
        # aroma_trait
        "None": 0,
        "Aromatic": 1,
        "Perfumy": 2,
        "Floral": 3,
        "Citrusy": 4,
        "Acrid": 5,
        "Fetid": 6,
        "Noxious": 7,
        "Musty": 8,
        "Max_Placeholder": 9,
        # sensation_trait
        "Cool": 1,
        "Warm": 2,
        "Bubbly": 3,
        "Velvety": 4,
        "Curdled": 5,
        "Greasy": 6,
        "Chalky": 7,
        "Stringy": 8,
        # sound_trait
        "Murmuring": 1,
        "Rustling": 2,
        "Fizzing": 3,
        "Purring": 4,
        "Gurgling": 5,
        "Noisy": 6,
        "Grating": 7,
        "Discordant": 8,
        # visual_trait
        "Sparkling": 1,
        "Colorful": 2,
        "Shimmering": 3,
        "Appetizing": 4,
        "Dull": 5,
        "Cloudy": 6,
        "Viscous": 7,
        "Moldy": 8,
        # taste_trait
        "Sweet": 1,
        "Savory": 2,
        "Spicy": 3,
        "Tangy": 4,
        "Bitter": 5,
        "Sour": 6,
        "Astringent": 7,
        "Bland": 8,
    }

    def _map_traits(self, src: dict):
        return {
            'Aroma': self.trait_map[src['AromaTrait'].replace("EAromaTrait::", '')],
            'Sensation': self.trait_map[src['SensationTrait'].replace("ESensationTrait::", '')],
            'Sound': self.trait_map[src['SoundTrait'].replace("ESoundTrait::", '')],
            'Visual': self.trait_map[src['VisualTrait'].replace("EVisualTrait::", '')],
            'Taste': self.trait_map[src['TasteTrait'].replace("EAromaTrait::", '')]
        }

    def _ingredient_to_list(self, ingredient: dict):
        metadata = resources.get_ingredient_metadata(ingredient['DataTableKey'])
        magimin = {'Red': 0, 'Green': 0, 'Yellow': 0, 'Blue': 0, 'Purple': 0}
        for e in ingredient['Elements']:
            magimin[e['Element']] = e['Quality']
        return {
            'NameKey': ingredient['DataTableKey'],
            'Name': metadata["name"],
            'LocalizationKey': metadata['localization_key'],
            'DropWeight': metadata['drop_weight'],
            'RelationshipValue': metadata['relationship_value'],
            'BasePrice': metadata['base_price'],
            'Biomes': [k[8:] for k in ingredient['Biomes']],
            'Category': ingredient['Category'],
            **magimin,
            **self._map_traits(ingredient)
        }

    def _ingredients_to_df(self, ingredients: list):
        if ingredients:
            data = [(self._ingredient_to_list(i['Ingredient']) | {'Quantity': i['Count']}) for i in
                    ingredients]
            return pd.DataFrame(data) \
                .astype(
                {'Name': 'string', 'Quantity': 'int32', 'Red': 'int32', 'Green': 'int32', 'Yellow': 'int32',
                 'Blue': 'int32', 'Purple': 'int32', 'Aroma': 'int32', 'Sensation': 'int32', 'Sound': 'int32',
                 'Visual': 'int32', 'Taste': 'int32', 'BasePrice': 'int32'})
        return None

    def get_ingredients(self) -> pd.DataFrame:
        return self._ingredients_to_df(self.raw_parsed['IngredientsInInventory'])

    def get_quinn_shop_inventory(self) -> pd.DataFrame:
        return self._ingredients_to_df(self.raw_parsed.get('DailyIngredients'))

    def _extract_potion(self, potion_item: dict) -> PotionData:
        """Extract potion data into a PotionData dataclass."""
        potion = potion_item.get('Potion', potion_item)
        
        # Use DataTableKey as the name - it's the actual identifier
        name = potion.get('DataTableKey', '')
        
        return PotionData(
            name=name,
            quantity=potion.get('Count', 0),
            rank=potion.get('Rank', ''),
            tier=potion.get('Tier', 0),
            star_rating=potion.get('StarValue', 0),
            traits=self._map_traits(potion)
        )

    def _extract_fuel_item(self, fuel_item: dict) -> dict:
        """Extract fuel data into a dictionary for DataFrame conversion."""
        fuel = fuel_item.get('Fuel', {})
        
        # Extract name from Text object
        name_data = fuel.get('Name', {})
        name = self._extract_text_name(name_data)
        
        return {
            'Name': name,
            'Price': fuel.get('Price', 0),
            'TimeSegmentsReduced': fuel.get('TimeSegmentsReduced', 0),
            'Quantity': fuel_item.get('Count', 0)
        }

    def get_potions(self) -> List[PotionData]:
        potions_data = self.raw_parsed.get('PotionsInInventory', [])
        return [self._extract_potion(p) for p in potions_data]

    def get_fuel(self) -> pd.DataFrame:
        fuel_data = self.raw_parsed.get('FuelInInventory', [])
        if fuel_data:
            data = [self._extract_fuel_item(f) for f in fuel_data]
            return pd.DataFrame(data).astype({
                'Name': 'string',
                'Price': 'int32',
                'TimeSegmentsReduced': 'int32',
                'Quantity': 'int32'
            })
        return None

    def get_world_history(self) -> dict[str, WorldState]:
        event_log_data = self.raw_parsed.get('EventLog', {})
        result = {}
        for event_name, event_data in event_log_data.items():
            if isinstance(event_data, dict):
                result[event_name] = WorldState(
                    day=event_data.get('Day', 0),
                    time_segments=event_data.get('TimeSegments', 0),
                    time_of_day=TimeOfDay(event_data['TimeOfDay']) if 'TimeOfDay' in event_data else self.DEFAULT_TIME_OF_DAY,
                    weather=Weather(event_data['Weather']) if 'Weather' in event_data else self.DEFAULT_WEATHER,
                    location=Location(event_data['Location']) if 'Location' in event_data else self.DEFAULT_LOCATION
                )
        return result

    def get_world_state(self) -> WorldState:
        src = self.raw_parsed['WorldState']
        return WorldState(
            day=src['Day'],
            time_segments=src.get('TimeSegments', 0),
            time_of_day = TimeOfDay(src['TimeOfDay']) if 'TimeOfDay' in src else self.DEFAULT_TIME_OF_DAY,
            weather=Weather(src['Weather']) if 'Weather' in src else self.DEFAULT_WEATHER,
            location=Location(src['Location']) if 'Location' in src else self.DEFAULT_LOCATION
        )

    def get_time_played(self) -> timedelta:
        return timedelta(seconds=self.raw_parsed['TimePlayed']['Timespan']/10000000.0)

    def get_romantic_relationship_type(self) -> Optional[RomanticRelationshipType]:
        return RomanticRelationshipType(self.raw_parsed['RomanticRelationshipType'])

    DEFAULT_TIME_OF_DAY = TimeOfDay.START_OF_DAY
    DEFAULT_WEATHER = Weather.SUNNY
    DEFAULT_LOCATION = Location.SYLVIA_SHOP
    raw_parsed: dict

    def __init__(self, json_file_name):
        super().__init__()
        self.raw_parsed = _load_from_json(json_file_name)

    def get_money(self) -> Optional[int]:
        return self.raw_parsed.get('Money')

    def get_baptiste_shop(self) -> Optional[BaptisteVendor]:
        src = self.raw_parsed.get('BaptisteInvestmentRequest')
        if src:
            return BaptisteVendor(
                ingredient_options=src['IngredientsSet_18_CF3EBE0D495042362CF857BD64F47582'],
                day=src['IngredientsSetGenerationDay_22_A48AC2904F6FCFAEDC8096820ABFAF64'],
                submitted_request_results={r['Ingredient_11_F8A6F25C4779815E8A7497BC97033B2F']: r['Quantity_10_5D0994B74A8190DF713A34B4433023D2'] for r in src['Request_15_5D0994B74A8190DF713A34B4433023D2']} if 'Request_15_5D0994B74A8190DF713A34B4433023D2' in src else None
            )
        return None

    def get_number_of_potions_brewed(self) -> Optional[int]:
        return self.raw_parsed.get('NumberOfPotionsBrewed')

    def get_gameplay_difficulty(self) -> Optional[GameplayDifficulty]:
        return GameplayDifficulty(self.raw_parsed['GameplayDifficulty'])

    def get_stress(self) -> int:
        return self.raw_parsed.get('Stress', 0)

    def get_card_library(self) -> List[str]:
        return self.raw_parsed.get('CardLibrary', [])

    def get_deck(self) -> List[str]:
        return self.raw_parsed.get('Deck', [])

    def get_stucco_walls(self) -> List[str]:
        return self.raw_parsed.get('StuccoWallOptions', [])

    def get_wood_walls(self) -> List[str]:
        return self.raw_parsed.get('WoodWallOptions', [])

    def get_flooring_options(self) -> List[str]:
        return self.raw_parsed.get('FlooringOptions', [])

    def _extract_cauldron(self, cauldron_data: dict) -> Cauldron:
        """Extract cauldron data into a Cauldron dataclass."""
        potion_data = None

        potion = None
        if 'BrewingDetails' in cauldron_data:
            potion = cauldron_data['BrewingDetails']['PotionBrewing']
            potion = self._extract_potion(potion)
        # if potion:
        #     name_data = potion.get('Name', '')
        #     name = self._extract_text_name(name_data)
        #     if not name:
        #         name = potion.get('DataTableKey', '')
        #
        #     rank_str = potion.get('Rank', '')
        #     if isinstance(rank_str, str) and '::' in rank_str:
        #         rank_str = rank_str.split('::')[-1]
        #
        #     potion_data = PotionData(
        #         name=name,
        #         quantity=potion.get('Quantity', 0),
        #         rank=rank_str,
        #         tier=potion.get('Tier', 0),
        #         star_rating=potion.get('StarValue', 0)
        #     )

        ingredients = []
        if 'IngredientsInCauldron' in cauldron_data:
            ingredients = [ing.get('DataTableKey', '') for ing in cauldron_data['IngredientsInCauldron']]

        # Get name from DataKey or Name field (BasementCauldrons use DataKey)
        name = cauldron_data.get('Name', '')
        if not name:
            data_key = cauldron_data.get('DataKey', '')
            name = data_key if isinstance(data_key, str) else ''

        return Cauldron(
            level=cauldron_data.get('Level', 0),
            actively_brewing=cauldron_data.get('ActivelyBrewing', False),
            potion=potion_data,
            name=name,
            ingredients=ingredients
        )

    def get_cauldrons_in_inventory(self) -> List[Cauldron]:
        cauldron_data = self.raw_parsed.get('CauldronOptions', [])
        return [self._extract_cauldron(c) for c in cauldron_data]

    def get_shop_cauldrons(self) -> List[Cauldron]:
        cauldron_data = self.raw_parsed.get('ShopCauldrons', [])
        return [self._extract_cauldron(c) for c in cauldron_data]

    def _extract_shelf(self, shelf_data: dict) -> Shelf:
        potions = []
        if 'PotionsOnShelf' in shelf_data:
            potions = [self._extract_potion(p) for p in shelf_data['PotionsOnShelf'] if p['DataTableKey'] != 'None']

        return Shelf(
            level=shelf_data.get('Level', 0),
            name=shelf_data['DataKey'],
            potions=potions
        )

    def get_front_display_shelves(self) -> List[Shelf]:
        shelf_data = self.raw_parsed.get('FrontDisplayShelves', [])
        return [self._extract_shelf(s) for s in shelf_data]

    def get_retail_counter_shelves(self) -> List[Shelf]:
        shelf_data = self.raw_parsed.get('RetailCounterShelves', [])
        return [self._extract_shelf(s) for s in shelf_data]

    def _extract_enchantment(self, enchant_data: dict) -> RoxanneEnchantment:
        return RoxanneEnchantment(
            duration=enchant_data['Duration'],
            cost=enchant_data['Cost'],
            key=self._extract_text_name(enchant_data['Name']),
            traits=self._map_traits(enchant_data['EnchantedTraits'])
        )

    def get_current_enchantment(self) -> Optional[RoxanneEnchantment]:
        enchant_data = self.raw_parsed.get('RoxCurrentEnchantment')
        if enchant_data and not enchant_data['Duration'] == 1115989024: # dummy values are located
            return self._extract_enchantment(enchant_data)
        return None

    def get_roxanne_shop_enchantments(self) -> List[RoxanneEnchantment]:
        enchant_list = self.raw_parsed.get('RoxDailyEnchantments', [])
        return [self._extract_enchantment(e) for e in enchant_list]

    def get_purchased_enchantment_today(self) -> bool:
        return self.raw_parsed.get('PurchasedEnchantmentToday', False)

    def get_heroes_in_party(self) -> dict[str, dict]:
        return self.raw_parsed.get('HeroesInParty', {})

    def get_events(self) -> List[EventOutcome]:
        daily_events = self.raw_parsed.get('DailyEventsLog', [])
        result = []
        for event_data in daily_events:
            event_key = event_data['DataKey']
            # Extract event type and convert to enum
            event_type_str = event_data['EventType'].split('::')[-1]
            result.append(EventOutcome(
                event_type=event_type_str,
                key=event_key,
                day=event_data['DayEventStarted'],
                duration=event_data['Duration'],
                outcomes={OutcomeType(k['OutcomeType'].split('::')[-1]): k['Args'] for k in event_data['Outcomes']}
            ))
        return result

    def _extract_marketing_plan(self, plan_data: dict) -> MarketingPlan:
        """Extract marketing plan data into a MarketingPlan dataclass."""
        name_data = plan_data.get('Name', {})
        name = self._extract_text_name(name_data)
        
        # Extract marketing outcome data key
        outcome_key_data = plan_data.get('MarketingOutcomeDataKey', '')
        outcome_key = outcome_key_data if isinstance(outcome_key_data, str) else ''
        
        return MarketingPlan(
            name=name,
            duration=plan_data.get('Duration', 0),
            cost=plan_data.get('Cost', 0),
            marketing_outcome_data_key=outcome_key
        )

    def get_marketing_plans(self) -> List[MarketingPlan]:
        marketing_plans = self.raw_parsed.get('DailyMarketingPlans', [])
        return [self._extract_marketing_plan(p) for p in marketing_plans]

    def get_active_marketing_plan(self) -> Optional[MarketingPlan]:
        plan_data = self.raw_parsed.get('ActiveLunaMarketingPlan')
        if plan_data:
            return self._extract_marketing_plan(plan_data)
        return None

    def _extract_slime_bulb(self, bulb_data: dict) -> SlimeBulb:
        """Extract slime bulb data into a SlimeBulb dataclass."""
        state_str = bulb_data.get('BulbState', '')
        if isinstance(state_str, str) and '::' in state_str:
            state_str = state_str.split('::')[-1]
        
        # Convert to enum
        try:
            state = SlimeBulbState(state_str)
        except (ValueError, KeyError):
            state = SlimeBulbState.IDLE
        
        # Extract seed ingredient with full details
        seed_ingredient = None
        seed_data = bulb_data.get('SeedIngredient', {})
        if isinstance(seed_data, dict):
            name_data = seed_data.get('Name', '')
            seed_name = self._extract_text_name(name_data)
            if not seed_name:
                seed_name = seed_data.get('DataTableKey', '')
            
            category = seed_data.get('Category', '')
            if isinstance(category, str) and '::' in category:
                category = category.split('::')[-1]
            
            # Extract optional ingredient fields
            volume = seed_data.get('Volume')
            biomes_data = seed_data.get('Biomes', [])
            biomes = [b if isinstance(b, str) else b.split('::')[-1] if '::' in str(b) else str(b) 
                     for b in (biomes_data if isinstance(biomes_data, list) else [])]
            elements = seed_data.get('Elements')
            
            # Convert trait strings to enums
            taste_trait_str = seed_data.get('TasteTrait', '')
            taste_trait = self._convert_enum_string(taste_trait_str, TasteTrait) if taste_trait_str else None
            
            sensation_trait_str = seed_data.get('SensationTrait', '')
            sensation_trait = self._convert_enum_string(sensation_trait_str, SensationTrait) if sensation_trait_str else None
            
            aroma_trait_str = seed_data.get('AromaTrait', '')
            aroma_trait = self._convert_enum_string(aroma_trait_str, AromaTrait) if aroma_trait_str else None
            
            visual_trait_str = seed_data.get('VisualTrait', '')
            visual_trait = self._convert_enum_string(visual_trait_str, VisualTrait) if visual_trait_str else None
            
            sound_trait_str = seed_data.get('SoundTrait', '')
            sound_trait = self._convert_enum_string(sound_trait_str, SoundTrait) if sound_trait_str else None
            
            tags_data = seed_data.get('Tags', [])
            tags = tags_data if isinstance(tags_data, list) else []
            
            seed_ingredient = Ingredient(
                name=seed_name,
                quantity=bulb_data.get('PreviousIngredientCount', 0),
                category=category,
                volume=volume,
                biomes=biomes if biomes else None,
                elements=elements,
                taste_trait=taste_trait,
                sensation_trait=sensation_trait,
                aroma_trait=aroma_trait,
                visual_trait=visual_trait,
                sound_trait=sound_trait,
                tags=tags if tags else None
            )
        
        # Extract start time if present
        start_time = None
        start_time_data = bulb_data.get('StartTime', {})
        if isinstance(start_time_data, dict):
            start_time = TimeStamp(
                day=start_time_data.get('Day', 0),
                time_segments=start_time_data.get('TimeSegments', 0)
            )
        
        bulb_name = f"Slime Bulb ({seed_data.get('DataTableKey', 'Unknown')})" if isinstance(seed_data, dict) else 'Slime Bulb'
        
        return SlimeBulb(
            name=bulb_name,
            seed_ingredient=seed_ingredient,
            state=state,
            growth_progress=bulb_data.get('CurrentIngredientCount', 0),
            start_time=start_time,
            food_magiment=bulb_data.get('FoodMagiment', 0),
            previous_ingredient_count=bulb_data.get('PreviousIngredientCount', 0),
            current_ingredient_count=bulb_data.get('CurrentIngredientCount', 0)
        )

    def get_slime_bulbs(self) -> List[SlimeBulb]:
        slime_bulbs = self.raw_parsed.get('SlimeBulbs', [])
        return [self._extract_slime_bulb(b) for b in slime_bulbs]

    def _extract_aging_barrel(self, barrel_data: dict) -> AgingBarrel:
        """Extract aging barrel data into an AgingBarrel dataclass."""
        potion_data = None
        aging_details = barrel_data.get('AgingDetails', {})
        
        if isinstance(aging_details, dict):
            potion = aging_details.get('PotionBeingAged', {})
            if potion and isinstance(potion, dict):
                name_data = potion.get('Name', '')
                name = self._extract_text_name(name_data)
                if not name:
                    name = potion.get('DataTableKey', '')
                
                potion_data = PotionData(
                    name=name,
                    quantity=potion.get('Quantity', 0) if isinstance(potion, dict) else 0,
                    rank=potion.get('Rank', '') if isinstance(potion, dict) else '',
                    tier=potion.get('Tier', 0) if isinstance(potion, dict) else 0,
                    star_rating=potion.get('StarValue', 0) if isinstance(potion, dict) else 0
                )
        
        # Extract state and convert to enum
        state_str = barrel_data.get('AgingBarrelState', '')
        if isinstance(state_str, str) and '::' in state_str:
            state_str = state_str.split('::')[-1]
        
        try:
            state = AgingBarrelState(state_str)
        except (ValueError, KeyError):
            state = AgingBarrelState.EMPTY
        
        # Extract start time if present
        start_time = None
        start_time_data = aging_details.get('StartingTimeStamp', {})
        if isinstance(start_time_data, dict):
            start_time = TimeStamp(
                day=start_time_data.get('Day', 0),
                time_segments=start_time_data.get('TimeSegments', 0)
            )
        
        data_key = barrel_data.get('DataKey', '')
        level = barrel_data.get('Level', 0)
        days_aging = aging_details.get('StartingTimeStamp', {}).get('Day', 0) if isinstance(aging_details, dict) else 0
        time_segments_to_age = aging_details.get('TimeSegmentsToAge', 0) if isinstance(aging_details, dict) else 0
        
        return AgingBarrel(
            data_key=data_key,
            level=level,
            state=state_str,
            potion=potion_data,
            start_time=start_time,
            days_aging=days_aging,
            time_segments_to_age=time_segments_to_age
        )

    def get_aging_barrels_in_inventory(self) -> List[AgingBarrel]:
        barrels = self.raw_parsed.get('AgingBarrelsInInventory', [])
        return [self._extract_aging_barrel(b) for b in barrels]

    def get_active_aging_barrels(self) -> List[AgingBarrel]:
        barrels = self.raw_parsed.get('AgingBarrels', [])
        return [self._extract_aging_barrel(b) for b in barrels]

    def get_basement_cauldrons(self) -> List[Cauldron]:
        cauldron_data = self.raw_parsed.get('BasementCauldrons', [])
        return [self._extract_cauldron(c) for c in cauldron_data]


