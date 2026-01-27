# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class PotionomicsSave(KaitaiStruct):

    class ActiveEventType(IntEnum):
        daily = 0
        luna_marketing_plan = 1
        baptiste_investment = 2
        max_placeholder = 3

    class AdventureLootType(IntEnum):
        ingredient = 0
        fuel = 1
        floor = 2
        wall = 3
        max_placeholder = 4

    class AgingBarrelState(IntEnum):
        add_potion = 0
        aging = 1
        age_complete = 2
        max_placeholder = 3

    class AromaTrait(IntEnum):
        no_value = 0
        aromatic = 1
        perfumy = 2
        floral = 3
        citrusy = 4
        acris = 5
        fetid = 6
        noxious = 7
        musty = 8
        max_placeholder = 9

    class Biome(IntEnum):
        no_value = 0
        enchanted_forest = 1
        mushroom_mire = 2
        bone_wastes = 3
        storm_plains = 4
        the_ocean_coasts = 5
        the_shadow_steppe = 6
        sulfuric_falls = 7
        crystaline_forest = 8
        ice_craggs = 9
        crater = 10
        dragon_oasis = 11
        the_artic = 12
        magic_wasteland = 13
        max_placeholder = 14

    class CauldronBrewState(IntEnum):
        add_ingredients = 0
        brewing = 1
        brew_complete = 2
        max_placeholder = 3

    class CauldronStability(IntEnum):
        too_unstable = 0
        unstable = 1
        stable = 2
        very_stable = 3
        perfect = 4
        max_placeholder = 5

    class Element(IntEnum):
        red = 0
        green = 1
        yellow = 2
        blue = 3
        purple = 4
        max_placeholder = 5

    class EventOutcomeType(IntEnum):
        no_value = 0
        increase_ingredient_value = 1
        decrease_ingredient_value = 2
        increase_ingredient_value_by_category = 3
        decrease_ingredient_value_by_category = 4
        increase_ingredient_value_by_biome = 5
        decrease_ingredient_value_by_biome = 6
        increase_potion_value = 7
        decrease_potion_value = 8
        increase_potion_value_by_category = 9
        decrease_potion_value_by_category = 10
        increase_potion_trait_value = 11
        decrease_potion_trait_value = 12
        increase_number_of_customers = 13
        decrease_number_of_customers = 14
        increase_customer_frequency_by = 15
        increase_customer_frequency_by_personality = 16
        debuff_customer = 17
        biome_supply_up = 18
        biome_supply_down = 19
        biome_raid = 20
        lock_biome = 21
        increase_ingredient_supply = 22
        decrease_ingredient_supply = 23
        increase_ingredient_supply_by_category = 24
        decrease_ingredient_supply_by_category = 25
        increase_ingredient_supply_by_biome = 26
        decrease_ingredient_supply_by_biome = 27
        increase_fuel_supply = 28
        decrease_fuel_supply = 29
        double_relationship_gains = 30
        potion_category_patent = 31
        max_placeholder = 32

    class IngredientCategory(IntEnum):
        slime = 0
        plant = 1
        flower = 2
        fruit = 3
        fungus = 4
        bug = 5
        fish = 6
        flesh = 7
        bone = 8
        mineral = 9
        essences = 10
        gem = 11
        ores = 12
        pure_mana = 13
        max_placeholder = 14

    class Location(IntEnum):
        sylvia_shop = 0
        counter = 1
        cauldron = 2
        overworld = 3
        quinn_shop = 4
        muktuk_shop = 5
        saffron_shop = 6
        saltnpepper_shop = 7
        roxanne = 8
        baptiste_guild = 9
        luna_shop = 10
        carnival = 11
        sylvia_basement = 12
        dialogue = 13
        mint_guild = 14
        corsac_guild = 15
        xid_guild = 16
        sylvia_shop_intro = 17
        carnival_final = 18
        sylvia_shop_nighttime = 19
        gardening = 20
        title = 21
        credits = 22
        max_placeholder = 23

    class PotionCategory(IntEnum):
        potions = 0
        tonics = 1
        enhancers = 2
        cures = 3
        max_placeholder = 4

    class PotionEffect(IntEnum):
        health = 0
        mana = 1
        stamina = 2
        drowsy = 3
        fire_resistance = 4
        ice_resistance = 5
        radiation_resistance = 6
        poison_resistance = 7
        sight = 8
        silence = 9
        speed = 10
        thunder_resistance = 11
        tolerance = 12
        petrification = 13
        alertness = 14
        curse_resistance = 15
        insight = 16
        seeker = 17
        shadow_resistance = 18
        dowsing = 19
        max_placeholder = 20

    class PotionRank(IntEnum):
        unranked = 0
        common = 1
        uncommon = 2
        rare = 3
        max_placeholder = 4

    class PotionTier(IntEnum):
        minor = 0
        common = 1
        greater = 2
        grand = 3
        superior = 4
        masterwork = 5

    class SensationTrait(IntEnum):
        no_value = 0
        cool = 1
        warm = 2
        bubbly = 3
        velvety = 4
        curdled = 5
        greasy = 6
        chalky = 7
        stringy = 8
        max_placeholder = 9

    class SlimeBulbState(IntEnum):
        idle = 0
        growing = 1
        ready_to_harvest = 2
        max_placeholder = 3

    class SoundTrait(IntEnum):
        no_value = 0
        murmuring = 1
        rustling = 2
        fizzing = 3
        purring = 4
        gurgling = 5
        noisy = 6
        grating = 7
        discordant = 8
        max_placeholder = 9

    class TasteTrait(IntEnum):
        no_value = 0
        sweet = 1
        savory = 2
        spicy = 3
        tangy = 4
        bitter = 5
        sour = 6
        astringent = 7
        bland = 8
        max_placeholder = 9

    class TimeOfDay(IntEnum):
        start_of_day = 0
        morning = 1
        afternoon = 2
        night = 3
        end_of_day = 4
        invalid = 5
        max_placeholder = 6

    class VisualTrait(IntEnum):
        no_value = 0
        sparkling = 1
        colorful = 2
        shimmering = 3
        appetizing = 4
        dull = 5
        cloudy = 6
        viscous = 7
        moldy = 8
        max_placeholder = 9

    class Weather(IntEnum):
        sunny = 0
        cloudy = 1
        partly_cloudy = 2
        rainy = 3
        snowy = 4
        sleeting = 5
        stormy = 6
        lightning = 7
        thunder = 8
        hailing = 9
        windy = 10
        foggy = 11
        icy = 12
        clear_sky = 13
        max_placeholder = 14
    def __init__(self, _io, _parent=None, _root=None):
        super(PotionomicsSave, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.world = PotionomicsSave.WorldState(self._io, self, self._root)
        self.gold = self._io.read_s4le()
        self._unnamed2 = self._io.read_u4le()
        self.number_of_potions_brewed = self._io.read_s4le()
        self.stress = self._io.read_s4le()
        self.active_chapter = self._io.read_u4le()
        self.num_ingredients = self._io.read_u4le()
        self.ingredients = []
        for i in range(self.num_ingredients):
            self.ingredients.append(PotionomicsSave.IngredientWithQuantity(self._io, self, self._root))

        self.num_potions = self._io.read_u4le()
        self.potions = []
        for i in range(self.num_potions):
            self.potions.append(PotionomicsSave.PotionWithQuantity(self._io, self, self._root))

        self.num_fuel = self._io.read_u4le()
        self.fuel = []
        for i in range(self.num_fuel):
            self.fuel.append(PotionomicsSave.FuelWithQuantity(self._io, self, self._root))

        self.num_event_flags = self._io.read_u4le()
        self.event_flags = []
        for i in range(self.num_event_flags):
            self.event_flags.append(PotionomicsSave.EventFlag(self._io, self, self._root))

        self.num_progress_flags = self._io.read_u4le()
        self.progress_flags = []
        for i in range(self.num_progress_flags):
            self.progress_flags.append(PotionomicsSave.ProgressFlag(self._io, self, self._root))

        self.num_completed_chapters = self._io.read_u4le()
        self.completed_chapters = []
        for i in range(self.num_completed_chapters):
            self.completed_chapters.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self.num_stucco_walls = self._io.read_u4le()
        self.stucco_walls = []
        for i in range(self.num_stucco_walls):
            self.stucco_walls.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self.num_wood_walls = self._io.read_u4le()
        self.wood_walls = []
        for i in range(self.num_wood_walls):
            self.wood_walls.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self.num_floors = self._io.read_u4le()
        self.floors = []
        for i in range(self.num_floors):
            self.floors.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self.num_inventory_display_shelves = self._io.read_u4le()
        self.inventory_display_shelves = []
        for i in range(self.num_inventory_display_shelves):
            self.inventory_display_shelves.append(PotionomicsSave.Shelf(self._io, self, self._root))

        self.num_inventory_shop_shelves = self._io.read_u4le()
        self.inventory_shop_shelves = []
        for i in range(self.num_inventory_shop_shelves):
            self.inventory_shop_shelves.append(PotionomicsSave.Shelf(self._io, self, self._root))

        self.num_inventory_cauldrons = self._io.read_u4le()
        self.inventory_cauldrons = []
        for i in range(self.num_inventory_cauldrons):
            self.inventory_cauldrons.append(PotionomicsSave.Cauldron(self._io, self, self._root))

        self.num_inventory_aging_barrels = self._io.read_u4le()
        self.inventory_aging_barrels = []
        for i in range(self.num_inventory_aging_barrels):
            self.inventory_aging_barrels.append(PotionomicsSave.AgingBarrel(self._io, self, self._root))

        self.num_past_events = self._io.read_u4le()
        self.past_events = []
        for i in range(self.num_past_events):
            self.past_events.append(PotionomicsSave.Event(self._io, self, self._root))

        self.num_unlocked_cards = self._io.read_u4le()
        self.unlocked_cards = []
        for i in range(self.num_unlocked_cards):
            self.unlocked_cards.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self.num_slime_bulbs = self._io.read_u4le()
        self.slime_bulbs = []
        for i in range(self.num_slime_bulbs):
            self.slime_bulbs.append(PotionomicsSave.SlimeBulb(self._io, self, self._root))

        self.num_heroes = self._io.read_u4le()
        self.heroes = []
        for i in range(self.num_heroes):
            self.heroes.append(PotionomicsSave.Hero(self._io, self, self._root))

        self.num_daily_stats = self._io.read_u4le()
        self.daily_stats = []
        for i in range(self.num_daily_stats):
            self.daily_stats.append(PotionomicsSave.DailyStats(self._io, self, self._root))

        self._unnamed42 = self._io.read_bytes(12)
        self.num_active_cauldrons = self._io.read_u4le()
        self.active_cauldrons = []
        for i in range(self.num_active_cauldrons):
            self.active_cauldrons.append(PotionomicsSave.Cauldron(self._io, self, self._root))

        self.num_inactive_cauldrons = self._io.read_u4le()
        self.inactive_cauldrons = []
        for i in range(self.num_inactive_cauldrons):
            self.inactive_cauldrons.append(PotionomicsSave.Cauldron(self._io, self, self._root))

        self.num_active_aging_barrels = self._io.read_u4le()
        self.active_aging_barrels = []
        for i in range(self.num_active_aging_barrels):
            self.active_aging_barrels.append(PotionomicsSave.AgingBarrel(self._io, self, self._root))

        self.num_active_display_shelves = self._io.read_u4le()
        self.active_display_shelves = []
        for i in range(self.num_active_display_shelves):
            self.active_display_shelves.append(PotionomicsSave.Shelf(self._io, self, self._root))

        self.num_active_shop_shelves = self._io.read_u4le()
        self.active_shop_shelves = []
        for i in range(self.num_active_shop_shelves):
            self.active_shop_shelves.append(PotionomicsSave.Shelf(self._io, self, self._root))

        self.active_glamours = []
        for i in range(4):
            self.active_glamours.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self._unnamed54 = self._io.read_bytes(4)
        self.num_friends = self._io.read_u4le()
        self.friends = []
        for i in range(self.num_friends):
            self.friends.append(PotionomicsSave.Friend(self._io, self, self._root))

        self.num_romances = self._io.read_u4le()
        self.romances = []
        for i in range(self.num_romances):
            self.romances.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self.num_hangouts = self._io.read_u4le()
        self.hangouts = []
        for i in range(self.num_hangouts):
            self.hangouts.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self.num_gifts_given = self._io.read_u4le()
        self.gifts_given = []
        for i in range(self.num_gifts_given):
            self.gifts_given.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self.num_quinn_unlocks = self._io.read_u4le()
        self.quinn_unlocks = []
        for i in range(self.num_quinn_unlocks):
            self.quinn_unlocks.append(PotionomicsSave.StrWithLen(self._io, self, self._root))

        self.num_quinn_shop_items = self._io.read_u4le()
        self.quinn_shop_items = []
        for i in range(self.num_quinn_shop_items):
            self.quinn_shop_items.append(PotionomicsSave.IngredientWithQuantity(self._io, self, self._root))

        self.ingredient_types_to_sell = self._io.read_s4le()
        self.ingredients_fed = self._io.read_s4le()
        self._unnamed69 = self._io.read_bytes(4)
        self.purchased_enchantment_today = self._io.read_u4le()
        self.active_enchantment = PotionomicsSave.RoxanneEnchantmentData(self._io, self, self._root)
        self._unnamed72 = self._io.read_bytes(4)
        self.num_roxanne_shop_enchantments = self._io.read_u4le()
        self.roxanne_shop_enchantments = []
        for i in range(self.num_roxanne_shop_enchantments):
            self.roxanne_shop_enchantments.append(PotionomicsSave.RoxanneEnchantmentData(self._io, self, self._root))

        self.num_saffron_shop_fuel = self._io.read_u4le()
        self.saffron_shop_fuel = []
        for i in range(self.num_saffron_shop_fuel):
            self.saffron_shop_fuel.append(PotionomicsSave.FuelWithQuantity(self._io, self, self._root))

        self._unnamed77 = self._io.read_bytes(4)
        self.num_active_daily_events = self._io.read_u4le()
        self.active_daily_events = []
        for i in range(self.num_active_daily_events):
            self.active_daily_events.append(PotionomicsSave.Event(self._io, self, self._root))

        self.vendor_active_events = []
        i = 0
        while not self._io.is_eof():
            self.vendor_active_events.append(PotionomicsSave.Event(self._io, self, self._root))
            i += 1



    def _fetch_instances(self):
        pass
        self.world._fetch_instances()
        for i in range(len(self.ingredients)):
            pass
            self.ingredients[i]._fetch_instances()

        for i in range(len(self.potions)):
            pass
            self.potions[i]._fetch_instances()

        for i in range(len(self.fuel)):
            pass
            self.fuel[i]._fetch_instances()

        for i in range(len(self.event_flags)):
            pass
            self.event_flags[i]._fetch_instances()

        for i in range(len(self.progress_flags)):
            pass
            self.progress_flags[i]._fetch_instances()

        for i in range(len(self.completed_chapters)):
            pass
            self.completed_chapters[i]._fetch_instances()

        for i in range(len(self.stucco_walls)):
            pass
            self.stucco_walls[i]._fetch_instances()

        for i in range(len(self.wood_walls)):
            pass
            self.wood_walls[i]._fetch_instances()

        for i in range(len(self.floors)):
            pass
            self.floors[i]._fetch_instances()

        for i in range(len(self.inventory_display_shelves)):
            pass
            self.inventory_display_shelves[i]._fetch_instances()

        for i in range(len(self.inventory_shop_shelves)):
            pass
            self.inventory_shop_shelves[i]._fetch_instances()

        for i in range(len(self.inventory_cauldrons)):
            pass
            self.inventory_cauldrons[i]._fetch_instances()

        for i in range(len(self.inventory_aging_barrels)):
            pass
            self.inventory_aging_barrels[i]._fetch_instances()

        for i in range(len(self.past_events)):
            pass
            self.past_events[i]._fetch_instances()

        for i in range(len(self.unlocked_cards)):
            pass
            self.unlocked_cards[i]._fetch_instances()

        for i in range(len(self.slime_bulbs)):
            pass
            self.slime_bulbs[i]._fetch_instances()

        for i in range(len(self.heroes)):
            pass
            self.heroes[i]._fetch_instances()

        for i in range(len(self.daily_stats)):
            pass
            self.daily_stats[i]._fetch_instances()

        for i in range(len(self.active_cauldrons)):
            pass
            self.active_cauldrons[i]._fetch_instances()

        for i in range(len(self.inactive_cauldrons)):
            pass
            self.inactive_cauldrons[i]._fetch_instances()

        for i in range(len(self.active_aging_barrels)):
            pass
            self.active_aging_barrels[i]._fetch_instances()

        for i in range(len(self.active_display_shelves)):
            pass
            self.active_display_shelves[i]._fetch_instances()

        for i in range(len(self.active_shop_shelves)):
            pass
            self.active_shop_shelves[i]._fetch_instances()

        for i in range(len(self.active_glamours)):
            pass
            self.active_glamours[i]._fetch_instances()

        for i in range(len(self.friends)):
            pass
            self.friends[i]._fetch_instances()

        for i in range(len(self.romances)):
            pass
            self.romances[i]._fetch_instances()

        for i in range(len(self.hangouts)):
            pass
            self.hangouts[i]._fetch_instances()

        for i in range(len(self.gifts_given)):
            pass
            self.gifts_given[i]._fetch_instances()

        for i in range(len(self.quinn_unlocks)):
            pass
            self.quinn_unlocks[i]._fetch_instances()

        for i in range(len(self.quinn_shop_items)):
            pass
            self.quinn_shop_items[i]._fetch_instances()

        self.active_enchantment._fetch_instances()
        for i in range(len(self.roxanne_shop_enchantments)):
            pass
            self.roxanne_shop_enchantments[i]._fetch_instances()

        for i in range(len(self.saffron_shop_fuel)):
            pass
            self.saffron_shop_fuel[i]._fetch_instances()

        for i in range(len(self.active_daily_events)):
            pass
            self.active_daily_events[i]._fetch_instances()

        for i in range(len(self.vendor_active_events)):
            pass
            self.vendor_active_events[i]._fetch_instances()


    class ActiveHeroPotionEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.ActiveHeroPotionEffect, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.effect = KaitaiStream.resolve_enum(PotionomicsSave.PotionEffect, self._io.read_u1())
            self.value = self._io.read_s4le()


        def _fetch_instances(self):
            pass


    class AgingBarrel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.AgingBarrel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.level = self._io.read_s4le()
            self.state = KaitaiStream.resolve_enum(PotionomicsSave.AgingBarrelState, self._io.read_u1())
            self.day_obtained = self._io.read_s4le()
            self.time_segment_obtained = self._io.read_s4le()
            self.time_segments_to_age = self._io.read_s4le()
            self.potion = PotionomicsSave.PotionWithQuantity(self._io, self, self._root)
            self.num_potion_placements = self._io.read_u4le()
            self.potion_placements = []
            for i in range(self.num_potion_placements):
                self.potion_placements.append(PotionomicsSave.XyPair(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            self.potion._fetch_instances()
            for i in range(len(self.potion_placements)):
                pass
                self.potion_placements[i]._fetch_instances()



    class Cauldron(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Cauldron, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.level = self._io.read_s4le()
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.actively_brewing = self._io.read_u4le()
            self.day_obtained = self._io.read_s4le()
            self.time_segment_obtained = self._io.read_s4le()
            self.time_segments_to_brew = self._io.read_s4le()
            self.potion = PotionomicsSave.PotionWithQuantity(self._io, self, self._root)
            self.num_ingredients = self._io.read_u4le()
            self.ingredients = []
            for i in range(self.num_ingredients):
                self.ingredients.append(PotionomicsSave.Ingredient(self._io, self, self._root))

            self.num_fuel = self._io.read_u4le()
            self.fuel = []
            for i in range(self.num_fuel):
                self.fuel.append(PotionomicsSave.Fuel(self._io, self, self._root))

            self.brew_state = KaitaiStream.resolve_enum(PotionomicsSave.CauldronBrewState, self._io.read_u1())
            self.num_ingredient_placements = self._io.read_u4le()
            self.ingredient_placements = []
            for i in range(self.num_ingredient_placements):
                self.ingredient_placements.append(PotionomicsSave.XyPair(self._io, self, self._root))

            self.stability = KaitaiStream.resolve_enum(PotionomicsSave.CauldronStability, self._io.read_u1())


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            self.potion._fetch_instances()
            for i in range(len(self.ingredients)):
                pass
                self.ingredients[i]._fetch_instances()

            for i in range(len(self.fuel)):
                pass
                self.fuel[i]._fetch_instances()

            for i in range(len(self.ingredient_placements)):
                pass
                self.ingredient_placements[i]._fetch_instances()



    class DailyStats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.DailyStats, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.number_of_customers = self._io.read_s4le()
            self.potions_sold = self._io.read_s4le()
            self.gold_spent = self._io.read_s4le()
            self.gold_earned = self._io.read_s4le()


        def _fetch_instances(self):
            pass


    class Event(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Event, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.type = KaitaiStream.resolve_enum(PotionomicsSave.ActiveEventType, self._io.read_u1())
            self.day_occurred = self._io.read_s4le()
            self.duration = self._io.read_s4le()
            self.num_outcomes = self._io.read_u4le()
            self.outcomes = []
            for i in range(self.num_outcomes):
                self.outcomes.append(PotionomicsSave.EventOutcome(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            for i in range(len(self.outcomes)):
                pass
                self.outcomes[i]._fetch_instances()



    class EventFlag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.EventFlag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.world_state = PotionomicsSave.WorldState(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            self.world_state._fetch_instances()


    class EventOutcome(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.EventOutcome, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(PotionomicsSave.EventOutcomeType, self._io.read_u1())
            self.num_args = self._io.read_u4le()
            self.args = []
            for i in range(self.num_args):
                self.args.append(PotionomicsSave.StrWithLen(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.args)):
                pass
                self.args[i]._fetch_instances()



    class Friend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Friend, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.level = self._io.read_s4le()
            self.current_friendship_points = self._io.read_s4le()
            self.flirt_level = self._io.read_s4le()
            self.hangout_level = self._io.read_s4le()
            self.num_coupons = self._io.read_s4le()
            self.coupons = []
            for i in range(self.num_coupons):
                self.coupons.append(PotionomicsSave.StrWithLen(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            for i in range(len(self.coupons)):
                pass
                self.coupons[i]._fetch_instances()



    class Fuel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Fuel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.localized_name = PotionomicsSave.LocTable(self._io, self, self._root)
            self.localized_description = PotionomicsSave.LocTable(self._io, self, self._root)
            self.time_segments_reduced = self._io.read_s4le()
            self.price = self._io.read_s4le()


        def _fetch_instances(self):
            pass
            self.localized_name._fetch_instances()
            self.localized_description._fetch_instances()


    class FuelWithQuantity(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.FuelWithQuantity, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.fuel = PotionomicsSave.Fuel(self._io, self, self._root)
            self.quantity = self._io.read_s4le()


        def _fetch_instances(self):
            pass
            self.fuel._fetch_instances()


    class Hero(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Hero, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name_key = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.level = self._io.read_s4le()
            self.experience = self._io.read_s4le()
            self.is_on_adventure = self._io.read_u4le()
            self.starting_day = self._io.read_s4le()
            self.starting_time_segment = self._io.read_s4le()
            self.time_segments_until_return = self._io.read_s4le()
            self.xp_to_gain = self._io.read_s4le()
            self.num_rewards = self._io.read_u4le()
            self.rewards = []
            for i in range(self.num_rewards):
                self.rewards.append(PotionomicsSave.Reward(self._io, self, self._root))

            self.adventure_result = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.num_equipped_potions = self._io.read_u4le()
            self.equipped_potions = []
            for i in range(self.num_equipped_potions):
                self.equipped_potions.append(PotionomicsSave.Potion(self._io, self, self._root))

            self.num_equipped_potion_effects = self._io.read_u4le()
            self.equipped_potion_effects = []
            for i in range(self.num_equipped_potion_effects):
                self.equipped_potion_effects.append(PotionomicsSave.ActiveHeroPotionEffect(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            self.name_key._fetch_instances()
            self.name._fetch_instances()
            for i in range(len(self.rewards)):
                pass
                self.rewards[i]._fetch_instances()

            self.adventure_result._fetch_instances()
            for i in range(len(self.equipped_potions)):
                pass
                self.equipped_potions[i]._fetch_instances()

            for i in range(len(self.equipped_potion_effects)):
                pass
                self.equipped_potion_effects[i]._fetch_instances()



    class Ingredient(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Ingredient, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.localized_name = PotionomicsSave.LocTable(self._io, self, self._root)
            self.localized_description = PotionomicsSave.LocTable(self._io, self, self._root)
            self.volume = self._io.read_s4le()
            self.num_biomes = self._io.read_u4le()
            self.biomes = []
            for i in range(self.num_biomes):
                self.biomes.append(KaitaiStream.resolve_enum(PotionomicsSave.Biome, self._io.read_u1()))

            self.category = KaitaiStream.resolve_enum(PotionomicsSave.IngredientCategory, self._io.read_u1())
            self.num_magimins = self._io.read_u4le()
            self.magimins = []
            for i in range(self.num_magimins):
                self.magimins.append(PotionomicsSave.Magimin(self._io, self, self._root))

            self.traits = PotionomicsSave.Traits(self._io, self, self._root)
            self.num_tags = self._io.read_u4le()
            self.tags = []
            for i in range(self.num_tags):
                self.tags.append(PotionomicsSave.StrWithLen(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            self.localized_name._fetch_instances()
            self.localized_description._fetch_instances()
            for i in range(len(self.biomes)):
                pass

            for i in range(len(self.magimins)):
                pass
                self.magimins[i]._fetch_instances()

            self.traits._fetch_instances()
            for i in range(len(self.tags)):
                pass
                self.tags[i]._fetch_instances()



    class IngredientWithQuantity(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.IngredientWithQuantity, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.ingredient = PotionomicsSave.Ingredient(self._io, self, self._root)
            self.quantity = self._io.read_u4le()


        def _fetch_instances(self):
            pass
            self.ingredient._fetch_instances()


    class LocTable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.LocTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self._unnamed0 = self._io.read_u4le()
            self.valid = self._io.read_u1()
            if self.valid == 255:
                pass
                self._unnamed2 = self._io.read_bytes(4)

            if self.valid != 255:
                pass
                self.path = PotionomicsSave.StrWithLen(self._io, self, self._root)

            if self.valid != 255:
                pass
                self.identifier = PotionomicsSave.StrWithLen(self._io, self, self._root)



        def _fetch_instances(self):
            pass
            if self.valid == 255:
                pass

            if self.valid != 255:
                pass
                self.path._fetch_instances()

            if self.valid != 255:
                pass
                self.identifier._fetch_instances()



    class Magimin(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Magimin, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(PotionomicsSave.Element, self._io.read_u1())
            self.quantity = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class Potion(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Potion, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.localized_name = PotionomicsSave.LocTable(self._io, self, self._root)
            self.localized_description = PotionomicsSave.LocTable(self._io, self, self._root)
            self.category = KaitaiStream.resolve_enum(PotionomicsSave.PotionCategory, self._io.read_u1())
            self.traits = PotionomicsSave.Traits(self._io, self, self._root)
            self.rank = KaitaiStream.resolve_enum(PotionomicsSave.PotionRank, self._io.read_u1())
            self.tier = KaitaiStream.resolve_enum(PotionomicsSave.PotionTier, self._io.read_s4le())
            self.star_rating = self._io.read_s4le()
            self.effect = KaitaiStream.resolve_enum(PotionomicsSave.PotionEffect, self._io.read_u1())
            self.adventuring_effect_value = self._io.read_s4le()
            self.adventure_effects_stack = self._io.read_s4le()
            self.was_barrel_aged = self._io.read_s4le()
            self.barrel_key = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.aging_multiplier = self._io.read_f4le()


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            self.localized_name._fetch_instances()
            self.localized_description._fetch_instances()
            self.traits._fetch_instances()
            self.barrel_key._fetch_instances()


    class PotionWithQuantity(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.PotionWithQuantity, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.potion = PotionomicsSave.Potion(self._io, self, self._root)
            self.quantity = self._io.read_s4le()


        def _fetch_instances(self):
            pass
            self.potion._fetch_instances()


    class ProgressFlag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.ProgressFlag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.value = self._io.read_u4le()


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class Reward(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Reward, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(PotionomicsSave.AdventureLootType, self._io.read_u1())
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.quantity = self._io.read_s4le()
            self.drop_weight = self._io.read_s4le()
            self.num_potion_effects = self._io.read_u4le()
            self.potion_effects = []
            for i in range(self.num_potion_effects):
                self.potion_effects.append(KaitaiStream.resolve_enum(PotionomicsSave.PotionEffect, self._io.read_u1()))



        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            for i in range(len(self.potion_effects)):
                pass



    class RoxanneEnchantmentData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.RoxanneEnchantmentData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.localized_name = PotionomicsSave.LocTable(self._io, self, self._root)
            self.localized_description = PotionomicsSave.LocTable(self._io, self, self._root)
            self.duration = self._io.read_s4le()
            self.cost = self._io.read_s4le()
            self.traits = PotionomicsSave.Traits(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.localized_name._fetch_instances()
            self.localized_description._fetch_instances()
            self.traits._fetch_instances()


    class Shelf(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Shelf, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.level = self._io.read_s4le()
            self.name = PotionomicsSave.StrWithLen(self._io, self, self._root)
            self.num_potions = self._io.read_u4le()
            self.potions = []
            for i in range(self.num_potions):
                self.potions.append(PotionomicsSave.Potion(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            for i in range(len(self.potions)):
                pass
                self.potions[i]._fetch_instances()



    class SlimeBulb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.SlimeBulb, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.state = KaitaiStream.resolve_enum(PotionomicsSave.SlimeBulbState, self._io.read_u1())
            self.seed_ingredient = PotionomicsSave.Ingredient(self._io, self, self._root)
            self.day = self._io.read_s4le()
            self.time_segment = self._io.read_s4le()
            self.magimins_used = self._io.read_s4le()
            self.previous_ingredient_count = self._io.read_s4le()
            self.current_ingredient_count = self._io.read_s4le()


        def _fetch_instances(self):
            pass
            self.seed_ingredient._fetch_instances()


    class StrWithLen(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.StrWithLen, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.len_data = self._io.read_u4le()
            self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_data), 0, False)).decode(u"UTF-8")


        def _fetch_instances(self):
            pass


    class Traits(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.Traits, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.taste = KaitaiStream.resolve_enum(PotionomicsSave.TasteTrait, self._io.read_u1())
            self.sensation = KaitaiStream.resolve_enum(PotionomicsSave.SensationTrait, self._io.read_u1())
            self.aroma = KaitaiStream.resolve_enum(PotionomicsSave.AromaTrait, self._io.read_u1())
            self.visual = KaitaiStream.resolve_enum(PotionomicsSave.VisualTrait, self._io.read_u1())
            self.sound = KaitaiStream.resolve_enum(PotionomicsSave.SoundTrait, self._io.read_u1())


        def _fetch_instances(self):
            pass


    class WorldState(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.WorldState, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.day = self._io.read_s4le()
            self.time_segment = self._io.read_s4le()
            self.time_of_day = KaitaiStream.resolve_enum(PotionomicsSave.TimeOfDay, self._io.read_u1())
            self.location = KaitaiStream.resolve_enum(PotionomicsSave.Location, self._io.read_u1())
            self.weather = KaitaiStream.resolve_enum(PotionomicsSave.Weather, self._io.read_u1())


        def _fetch_instances(self):
            pass


    class XyPair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(PotionomicsSave.XyPair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()


        def _fetch_instances(self):
            pass



