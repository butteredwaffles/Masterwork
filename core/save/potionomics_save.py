from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Optional, List
import pandas as pd

class GameplayDifficulty(Enum):
    EASY = 'Easy'
    NORMAL = 'Normal'
    HARD = 'Hard'

class RomanticRelationshipType(Enum):
    MONOGAMY = 'Monogamy'
    POLYAMORY = 'Polyamory'

class TimeOfDay(Enum):
    START_OF_DAY = 'StartOfDay'
    MORNING = 'Morning'
    AFTERNOON = 'Afternoon'
    NIGHT = 'Night'
    END_OF_DAY = 'EndOfDay'

class Location(Enum):
    SYLVIA_SHOP = 'SylviasShop'
    COUNTER = 'Counter'
    CAULDRON = 'Cauldron'
    OVERWORLD = 'Overworld'
    QUINN_SHOP = 'QuinnsShop'
    MUKTUK_SHOP = 'MukTuksShop'
    SAFFRON_SHOP = 'DruidWitch'
    SALTNPEPPER_SHOP = 'SaltNPepper'
    ROXANNE_SHOP = 'Roxanne'
    BAPTISTE_SHOP = 'HeroGuildBar'
    LUNA_SHOP = 'MothGirl'
    TOURNAMENT = 'Carnival'
    SYLVIA_BASEMENT = 'SylviasBasement'
    DIALOGUE = 'Dialogue'
    MINT_GUILD = 'HeroGuildBar_Mint'
    CORSAC_GUILD = 'HeroGuildBar_Corsac'
    XID_GUILD = 'HeroGuildBar_Xid'
    SYLVIA_SHOP_INTRO = 'SylviaShopIntro'
    FINAL_TOURNAMENT = 'CarnivalFinal'
    SYLVIA_SHOP_NIGHTTIME = 'SylviasShopNighttime'
    GARDENING = 'Gardening'
    TITLE = 'Title'
    CREDITS = 'Credits'
    BOSS_FINN_SHOP = 'BossFinn'

class Weather(Enum):
    SUNNY = 'Sunny'
    CLOUDY = 'Cloudy'
    PARTLY_CLOUDY = 'PartlyCloudy'
    RAINY = 'Rainy'
    SNOWY = 'Snowy'
    SLEETING = 'Sleeting'
    STORMY = 'Storymy'
    LIGHTNING = 'Lightning'
    THUNDER = 'Thunder'
    HAILING = 'Hailing'
    WINDY = 'Windy'
    FOGGY = 'Foggy'
    ICY = 'Icy'
    CLEAR = 'ClearSky'

class SlimeBulbState(Enum):
    IDLE = 'Idle'
    GROWING = 'Growing'
    READY_TO_HARVEST = 'ReadyToHarvest'

class TasteTrait(Enum):
    NONE = 'None'
    SWEET = 'Sweet'
    SAVORY = 'Savory'
    SPICY = 'Spicy'
    TANGY = 'Tangy'
    BITTER = 'Bitter'
    SOUR = 'Sour'
    ASTRINGENT = 'Astringent'
    BLAND = 'Bland'

class SensationTrait(Enum):
    NONE = 'None'
    COOL = 'Cool'
    WARM = 'Warm'
    BUBBLY = 'Bubbly'
    VELVETY = 'Velvety'
    CURDLED = 'Curdled'
    GREASY = 'Greasy'
    CHALKY = 'Chalky'
    STRINGY = 'Stringy'

class AromaTrait(Enum):
    NONE = 'None'
    AROMATIC = 'Aromatic'
    PERFUMY = 'Perfumy'
    FLORAL = 'Floral'
    CITRUSY = 'Citrusy'
    ACRIS = 'Acris'
    FETID = 'Fetid'
    NOXIOUS = 'Noxious'
    MUSTY = 'Musty'
    MAX_PLACEHOLDER = 'Max_Placeholder'

class VisualTrait(Enum):
    NONE = 'None'
    SPARKLING = 'Sparkling'
    COLORFUL = 'Colorful'
    SHIMMERING = 'Shimmering'
    APPETIZING = 'Appetizing'
    DULL = 'Dull'
    CLOUDY = 'Cloudy'
    VISCOUS = 'Viscous'
    MOLDY = 'Moldy'

class SoundTrait(Enum):
    NONE = 'None'
    MURMURING = 'Murmuring'
    RUSTLING = 'Rustling'
    FIZZING = 'Fizzing'
    PURRING = 'Purring'
    GURGLING = 'Gurgling'
    NOISY = 'Noisy'
    GRATING = 'Grating'
    DISCORDANT = 'Discordant'

class AgingBarrelState(Enum):
    ADD_POTION = 'AddPotion'
    AGING = 'Aging'
    READY = 'Ready'
    EMPTY = 'Empty'

class PotionEffect(Enum):
    HEALTH = 'Health'
    MANA = 'Mana'
    STRENGTH = 'Strength'
    DEFENSE = 'Defense'
    SPEED = 'Speed'
    LUCK = 'Luck'

class OutcomeType(Enum):
    NONE = 'None'
    INCREASE_INGREDIENT_VALUE = 'IncreaseIngredientValue'
    DECREASE_INGREDIENT_VALUE = 'DecreaseIngredientValue'
    INCREASE_INGREDIENT_VALUE_BY_CATEGORY = 'IncreaseIngredientValueByCategory'
    DECREASE_INGREDIENT_VALUE_BY_CATEGORY = 'DecreaseIngredientValueByCategory'
    INCREASE_INGREDIENT_VALUE_BY_BIOME = 'IncreaseIngredientValueByBiome'
    DECREASE_INGREDIENT_VALUE_BY_BIOME = 'DecreaseIngredientValueByBiome'
    INCREASE_POTION_VALUE = 'IncreasePotionValue'
    DECREASE_POTION_VALUE = 'DecreasePotionValue'
    INCREASE_POTION_VALUE_BY_CATEGORY = 'IncreasePotionValueByCategory'
    DECREASE_POTION_VALUE_BY_CATEGORY = 'DecreasePotionValueByCategory'
    INCREASE_POTION_TRAIT_VALUE = 'IncreasePotionTraitValue'
    DECREASE_POTION_TRAIT_VALUE = 'DecreasePotionTraitValue'
    INCREASE_NUMBER_OF_CUSTOMERS = 'IncreaseNumberOfCustomers'
    DECREASE_NUMBER_OF_CUSTOMERS = 'DecreaseNumberOfCustomers'
    INCREASE_CUSTOMER_FREQUENCY_BY_CLASS = 'IncreaseCustomerFrequencyByClass'
    INCREASE_CUSTOMER_FREQUENCY_BY_PERSONALITY = 'IncreaseCustomerFrequencyByPersonality'
    DEBUFF_CUSTOMER = 'DebuffCustomer'
    BIOME_SUPPLY_UP = 'BiomeSupplyUp'
    BIOME_SUPPLY_DOWN = 'BiomeSupplyDown'
    BIOME_RAID = 'BiomeRaid'
    LOCK_BIOME = 'LockBiome'
    INCREASE_INGREDIENT_SUPPLY = 'IncreaseIngredientSupply'
    DECREASE_INGREDIENT_SUPPLY = 'DecreaseIngredientSupply'
    INCREASE_INGREDIENT_SUPPLY_BY_CATEGORY = 'IncreaseIngredientSupplyByCategory'
    DECREASE_INGREDIENT_SUPPLY_BY_CATEGORY = 'DecreaseIngredientSupplyByCategory'
    INCREASE_INGREDIENT_SUPPLY_BY_BIOME = 'IncreaseIngredientSupplyByBiome'
    DECREASE_INGREDIENT_SUPPLY_BY_BIOME = 'DecreaseIngredientSupplyByBiome'
    INCREASE_FUEL_SUPPLY = 'IncreaseFuelSupply'
    DECREASE_FUEL_SUPPLY = 'DecreaseFuelSupply'
    DOUBLE_RELATIONSHIP_GAINS = 'DoubleRelationshipGains'
    POTION_CATEGORY_PATENT = 'PotionCategoryPatent'

@dataclass
class BaptisteVendor:
    ingredient_options: List[str]
    day: int
    submitted_request_results: Optional[dict[str, int]]

@dataclass
class WorldState:
    day: int
    time_segments: int
    time_of_day: TimeOfDay
    location: Location
    weather: Weather

@dataclass
class DailyStats:
    money_earned: int
    money_spent: int
    number_of_customers: int
    potions_sold: int

@dataclass
class Relationship:
    num_coupons: int
    flirt_points: int
    hangout_level: int
    level: int
    value: int

@dataclass
class FuelData:
    name: str
    quantity: int
    time_segments_reduced: int
    price: int

@dataclass
class Ingredient:
    name: str
    quantity: int
    category: str
    volume: Optional[int] = None
    biomes: Optional[List[str]] = None
    elements: Optional[dict] = None
    taste_trait: Optional[TasteTrait] = None
    sensation_trait: Optional[SensationTrait] = None
    aroma_trait: Optional[AromaTrait] = None
    visual_trait: Optional[VisualTrait] = None
    sound_trait: Optional[SoundTrait] = None
    tags: Optional[List[str]] = None

@dataclass
class TimeStamp:
    day: int
    time_segments: int

@dataclass
class PotionData:
    name: str
    quantity: int
    rank: str
    tier: str
    star_rating: int
    traits: dict

@dataclass
class Shelf:
    level: int
    name: str
    potions: List[str]

@dataclass
class Cauldron:
    level: int
    actively_brewing: bool
    potion: Optional[PotionData]
    name: str = ''
    ingredients: List[str] = None

@dataclass
class RoxanneEnchantment:
    duration: int
    cost: int
    key: str
    traits: dict

@dataclass
class EventOutcome:
    event_type: str
    key: str
    day: int
    duration: int
    outcomes: list[dict[OutcomeType, list]]

@dataclass
class MarketingPlan:
    name: str
    duration: int
    cost: int
    marketing_outcome_data_key: str

@dataclass
class SlimeBulb:
    name: str
    seed_ingredient: Optional[Ingredient]
    state: SlimeBulbState
    growth_progress: int
    start_time: Optional[TimeStamp] = None
    food_magiment: int = 0
    previous_ingredient_count: int = 0
    current_ingredient_count: int = 0

@dataclass
class AgingBarrel:
    data_key: str
    level: int
    state: AgingBarrelState
    potion: Optional[PotionData] = None
    start_time: Optional[TimeStamp] = None
    days_aging: int = 0
    time_segments_to_age: int = 0




class PotionomicsSave(ABC):
    @abstractmethod
    def get_money(self) -> Optional[int]:
        pass
    @abstractmethod
    def get_baptiste_shop(self) -> Optional[BaptisteVendor]:
        pass
    @abstractmethod
    def get_number_of_potions_brewed(self) -> Optional[int]:
        pass
    @abstractmethod
    def get_gameplay_difficulty(self) -> Optional[GameplayDifficulty]:
        pass
    @abstractmethod
    def get_romantic_relationship_type(self) -> Optional[RomanticRelationshipType]:
        pass
    @abstractmethod
    def get_world_state(self) -> WorldState:
        pass
    @abstractmethod
    def get_flags(self) -> dict[str, bool]:
        pass
    @abstractmethod
    def get_active_chapter(self) -> int:
        pass
    @abstractmethod
    def get_daily_stats(self) -> List[DailyStats]:
        pass
    @abstractmethod
    def get_relationships(self) -> dict[str, Relationship]:
        pass
    @abstractmethod
    def get_time_played(self) -> timedelta:
        pass
    @abstractmethod
    def get_ingredients(self) -> pd.DataFrame:
        pass
    @abstractmethod
    def get_quinn_shop_inventory(self) -> pd.DataFrame:
        pass
    @abstractmethod
    def get_potions(self) -> List[PotionData]:
        pass
    @abstractmethod
    def get_fuel(self) -> pd.DataFrame:
        pass
    @abstractmethod
    def get_world_history(self) -> dict[str, WorldState]:
        pass
    @abstractmethod
    def get_events(self) -> List[EventOutcome]:
        pass
    @abstractmethod
    def get_stress(self) -> int:
        pass
    @abstractmethod
    def get_card_library(self) -> List[str]:
        pass
    @abstractmethod
    def get_deck(self) -> List[str]:
        pass
    @abstractmethod
    def get_stucco_walls(self) -> List[str]:
        pass
    @abstractmethod
    def get_wood_walls(self) -> List[str]:
        pass
    @abstractmethod
    def get_flooring_options(self) -> List[str]:
        pass
    @abstractmethod
    def get_cauldrons_in_inventory(self) -> List[Cauldron]:
        pass
    @abstractmethod
    def get_shop_cauldrons(self) -> List[Cauldron]:
        pass
    @abstractmethod
    def get_front_display_shelves(self) -> List[Shelf]:
        pass
    @abstractmethod
    def get_retail_counter_shelves(self) -> List[Shelf]:
        pass
    @abstractmethod
    def get_current_enchantment(self) -> Optional[RoxanneEnchantment]:
        pass
    @abstractmethod
    def get_roxanne_shop_enchantments(self) -> List[RoxanneEnchantment]:
        pass
    @abstractmethod
    def get_purchased_enchantment_today(self) -> bool:
        pass
    @abstractmethod
    def get_heroes_in_party(self) -> dict[str, dict]:
        pass
    @abstractmethod
    def get_marketing_plans(self) -> List[MarketingPlan]:
        pass
    @abstractmethod
    def get_active_marketing_plan(self) -> Optional[MarketingPlan]:
        pass
    @abstractmethod
    def get_aging_barrels_in_inventory(self) -> List[AgingBarrel]:
        pass
    @abstractmethod
    def get_active_aging_barrels(self) -> List[AgingBarrel]:
        pass
    @abstractmethod
    def get_slime_bulbs(self) -> List[SlimeBulb]:
        pass
    @abstractmethod
    def get_basement_cauldrons(self) -> List[Cauldron]:
        pass