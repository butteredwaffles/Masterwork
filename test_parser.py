import pytest
import json
from datetime import timedelta

from core.save.potionomics_save import TimeOfDay, Location, Weather
from parser.ue_save_parser import PotionomicsUESaveParser


@pytest.fixture
def save_parser():
    return PotionomicsUESaveParser('core/save/test3.json')


@pytest.fixture
def test3_json():
    with open('core/save/test3.json', 'r') as f:
        return json.load(f)

def _get_int(src: dict) -> int:
    return src['Int']

def _get_enum(src: dict) -> str:
    return src['Enum'].split('::')[-1]

def _get_str(src: dict) -> str:
    return src['Str']

class TestPotionomicsUESaveParser:
    """Test suite for PotionomicsUESaveParser abstract methods."""

    def test_get_money(self, save_parser, test3_json):
        money = save_parser.get_money()
        expected_money = test3_json['root']['properties']['Money_0']['Int']
        assert money == expected_money

    def test_get_number_of_potions_brewed(self, save_parser, test3_json):
        count = save_parser.get_number_of_potions_brewed()
        expected_count = _get_int(test3_json['root']['properties']['NumberOfPotionsBrewed_0'])
        assert count == expected_count

    def test_get_active_chapter(self, save_parser, test3_json):
        chapter = save_parser.get_active_chapter()
        expected_chapter = _get_int(test3_json['root']['properties']['ActiveChapter_0'])
        assert chapter == expected_chapter

    def test_get_gameplay_difficulty(self, save_parser, test3_json):
        difficulty = save_parser.get_gameplay_difficulty()
        expected_value = _get_enum(test3_json['root']['properties']['GameplayDifficulty_0'])
        assert difficulty.value == expected_value

    def test_get_romantic_relationship_type(self, save_parser, test3_json):
        rel_type = save_parser.get_romantic_relationship_type()
        expected_value = _get_enum(test3_json['root']['properties']['RomanticRelationshipType_0'])
        assert rel_type.value == expected_value

    def test_get_flags(self, save_parser, test3_json):
        flags = save_parser.get_flags()
        expected_flags_raw = test3_json['root']['properties']['Flags_0']['Map']
        expected_length = len(expected_flags_raw)
        assert len(flags) == expected_length

    def test_get_time_played(self, save_parser, test3_json):
        time_played = save_parser.get_time_played()
        expected_timespan = test3_json['root']['properties']['TimePlayed_0']['Struct']['Timespan']
        # Timespan is in 100-nanosecond intervals, convert to microseconds
        expected_timedelta = timedelta(microseconds=expected_timespan / 10)
        assert time_played == expected_timedelta

    def test_get_daily_stats(self, save_parser, test3_json):
        stats = save_parser.get_daily_stats()
        expected_stats_raw = test3_json['root']['properties']['DailyStats_0']['Array']['Struct']['value']
        assert len(stats) == len(expected_stats_raw)
        if len(stats) > 0:
            expected = expected_stats_raw[0]['Struct']
            assert stats[0].money_earned == _get_int(expected['GoldEarned_0'])
            assert stats[0].money_spent == _get_int(expected['GoldSpent_0'])
            assert stats[0].number_of_customers == _get_int(expected['NumberOfCustomers_0'])
            assert stats[0].potions_sold == _get_int(expected['PotionsSold_0'])

    def test_get_relationships(self, save_parser, test3_json):
        relationships = save_parser.get_relationships()
        expected_relationships = test3_json['root']['properties']['Relationships_0']['Map']
        assert len(relationships) == len(expected_relationships)

        expected = expected_relationships[0]
        assert _get_str(expected['key']) in relationships
        rel = relationships[_get_str(expected['key'])]
        exp_data = expected['value']['Struct']['Struct']
        assert rel.num_coupons == len(exp_data['CouponDataKeys_0']['Array']['Base']['Name'])
        assert rel.flirt_points == _get_int(exp_data['FlirtPoints_0'])
        assert rel.hangout_level == _get_int(exp_data['HangoutLevel_0'])
        assert rel.level == _get_int(exp_data['Level_0'])
        assert rel.value == _get_int(exp_data['Value_0'])


    # TODO: Add another test using a save that is not at the start of the day.
    def test_get_world_state(self, save_parser, test3_json):
        world_state = save_parser.get_world_state()
        expected = test3_json['root']['properties']['WorldState_0']['Struct']['Struct']
        assert world_state.day == _get_int(expected['Day_0'])
        assert world_state.time_segments == 0
        assert world_state.time_of_day == TimeOfDay.START_OF_DAY
        assert world_state.location == Location.SYLVIA_SHOP
        assert world_state.weather == Weather.SUNNY

    # TODO: Add test for save file with stress, this one has 0%
    def test_get_stress(self, save_parser, test3_json):
        stress = save_parser.get_stress()
        #expected_stress = _get_int(test3_json['root']['properties']['Stress_0'])
        assert stress == 0

    def test_get_card_library(self, save_parser, test3_json):
        cards = save_parser.get_card_library()
        expected_cards = test3_json['root']['properties']['CardLibrary_0']['Array']['Base']['Name']
        assert cards == expected_cards

    def test_get_deck(self, save_parser, test3_json):
        deck = save_parser.get_deck()
        expected_deck = test3_json['root']['properties']['Deck_0']['Array']['Base']['Name']
        assert deck == expected_deck

    def test_get_stucco_walls(self, save_parser, test3_json):
        walls = save_parser.get_stucco_walls()
        expected_walls = test3_json['root']['properties']['StuccoWallOptions_0']['Array']['Base']['Name']
        assert walls == expected_walls

    def test_get_wood_walls(self, save_parser, test3_json):
        walls = save_parser.get_wood_walls()
        expected_walls = test3_json['root']['properties']['WoodWallOptions_0']['Array']['Base']['Name']
        assert walls == expected_walls

    def test_get_flooring_options(self, save_parser, test3_json):
        flooring = save_parser.get_flooring_options()
        expected_flooring = test3_json['root']['properties']['FlooringOptions_0']['Array']['Base']['Name']
        assert flooring == expected_flooring

    def test_get_cauldrons_in_inventory(self, save_parser, test3_json):
        cauldrons = save_parser.get_cauldrons_in_inventory()
        expected_cauldrons = test3_json['root']['properties']['CauldronOptions_0']['Array']['Struct']['value']
        assert len(cauldrons) == len(expected_cauldrons)
        exp_value = expected_cauldrons[0]['Struct']
        caul = cauldrons[0]
        assert caul.level == _get_int(exp_value['Level_0'])
        assert caul.actively_brewing == exp_value['ActivelyBrewing_0']['Bool']
        assert caul.name == exp_value['DataKey_0']['Name']
        assert caul.potion is None
        assert len(caul.ingredients) == 0

    def test_get_shop_cauldrons(self, save_parser, test3_json):
        cauldrons = save_parser.get_shop_cauldrons()
        expected_cauldrons = test3_json['root']['properties']['ShopCauldrons_0']['Array']['Struct']['value']
        assert len(cauldrons) == len(expected_cauldrons)

    def test_get_front_display_shelves(self, save_parser, test3_json):
        shelves = save_parser.get_front_display_shelves()
        expected_shelves = test3_json['root']['properties']['FrontDisplayShelves_0']['Array']['Struct']['value']
        assert len(shelves) == len(expected_shelves)

    def test_get_retail_counter_shelves(self, save_parser, test3_json):
        shelves = save_parser.get_retail_counter_shelves()
        expected_shelves = test3_json['root']['properties']['RetailCounterShelves_0']['Array']['Struct']['value']
        assert len(shelves) == len(expected_shelves)

    # TODO: Add test with save with an active enchantment
    def test_get_current_enchantment(self, save_parser, test3_json):
        enchantment = save_parser.get_current_enchantment()
        expected_enchantment = test3_json['root']['properties'].get('CurrentEnchantment_0', {}).get('Struct', {})
        if expected_enchantment:
            assert enchantment is not None
        else:
            assert enchantment is None

    def test_get_roxanne_shop_enchantments(self, save_parser, test3_json):
        enchantments = save_parser.get_roxanne_shop_enchantments()
        expected_enchantments = test3_json['root']['properties']['RoxDailyEnchantments_0']['Array']['Struct']['value']
        assert len(enchantments) == len(expected_enchantments)


    # TODO: Add test for when an enchantment was purchased
    def test_get_purchased_enchantment_today(self, save_parser, test3_json):
        purchased = save_parser.get_purchased_enchantment_today()
        assert not purchased
        # expected_purchased = test3_json['root']['properties']['PurchasedEnchantmentToday_0']['Bool']
        # assert purchased == expected_purchased

    def test_get_heroes_in_party(self, save_parser, test3_json):
        """Test heroes in party."""
        heroes = save_parser.get_heroes_in_party()
        expected_heroes = test3_json['root']['properties']['HeroesInParty_0']['Map']
        assert len(heroes) == len(expected_heroes)

    def test_get_ingredients(self, save_parser, test3_json):
        """Test ingredients dataframe."""
        ingredients = save_parser.get_ingredients()
        expected_ingredients = test3_json['root']['properties']['IngredientsInInventory_0']['Array']['Struct']['value']
        assert len(ingredients) == len(expected_ingredients)

    def test_get_quinn_shop_inventory(self, save_parser, test3_json):
        """Test Quinn shop inventory."""
        inventory = save_parser.get_quinn_shop_inventory()
        expected_inventory = test3_json['root']['properties']['DailyIngredients_0']['Array']['Struct']['value']
        assert len(inventory) == len(expected_inventory)

    def test_get_potions(self, save_parser, test3_json):
        """Test potions list."""
        potions = save_parser.get_potions()
        expected_potions = test3_json['root']['properties']['PotionsInInventory_0']['Array']['Struct']['value']
        assert len(potions) == len(expected_potions)

    def test_get_fuel(self, save_parser, test3_json):
        fuel = save_parser.get_fuel()
        expected_fuel = test3_json['root']['properties']['FuelInInventory_0']['Array']['Struct']['value']
        assert len(fuel) == len(expected_fuel)

    def test_get_world_history(self, save_parser, test3_json):
        history = save_parser.get_world_history()
        expected_history = test3_json['root']['properties']['EventLog_0']['Map']
        assert len(history) == len(expected_history)

    def test_get_events(self, save_parser, test3_json):
        events = save_parser.get_events()
        expected_events = test3_json['root']['properties']['DailyEventsLog_0']['Array']['Struct']['value']
        assert len(events) == len(expected_events)

    def test_get_marketing_plans(self, save_parser, test3_json):
        plans = save_parser.get_marketing_plans()
        expected_plans = test3_json['root']['properties']['DailyMarketingPlans_0']['Array']['Struct']['value']
        assert len(plans) == len(expected_plans)

    def test_get_active_marketing_plan(self, save_parser, test3_json):
        plan = save_parser.get_active_marketing_plan()
        expected_plan = test3_json['root']['properties']['ActiveLunaMarketingPlan_0']['Struct']['Struct']
        if expected_plan:
            assert plan is not None
            assert plan.duration == expected_plan['Duration_0']['Int']
            assert plan.cost == expected_plan['Cost_0']['Int']
            assert plan.marketing_outcome_data_key == expected_plan['MarketingOutcomeDataKey_0']['Name']
        else:
            assert plan is None

    # TODO: Add Baptiste shop with submitted daily request test
    def test_get_baptiste_shop(self, save_parser, test3_json):
        """Test Baptiste shop."""
        shop = save_parser.get_baptiste_shop()
        expected_shop = test3_json['root']['properties'].get('BaptisteInvestmentRequest_0', {}).get('Struct', {})
        if expected_shop:
            assert shop is not None
        else:
            assert shop is None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
