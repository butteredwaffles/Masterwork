from pathlib import Path
import json

RESOURCE_DIR = Path('resources')
with open(RESOURCE_DIR / 'ingredients.json', 'r') as f:
    all_ingredients = json.load(f)

with open(RESOURCE_DIR / 'potions.json', 'r') as f:
    all_potions = json.load(f)

with open(RESOURCE_DIR / 'cauldrons.json', 'r') as f:
    all_cauldrons = json.load(f)

def get_ingredient_metadata(key: str) -> dict:
    """
    This function retrieves information about ingredients that are not stored as part of
    the save data.

    :param key: The internal key used for this item.
    :return:
    """
    ing = all_ingredients[key]
    return {
        "name": ing["Name"]["LocalizedString"],
        "localization_key": ing["Name"]["Key"],
        "drop_weight": ing["RandomDropWeight"],
        "relationship_value": ing["RelationshipPointsEarnedWhenGifted"],
        "base_price": ing["BasePrice"]
    }

def get_potion_metadata(key: str) -> dict:
    """
    This function retrieves information about potions that are not stored as part of
    the save data.

    :param key: The internal key used for this item.
    :return:
    """
    potion = all_potions[key]
    return {
        "name": potion["name"],
        "target_ratio": potion["target_ratio"],
        "brew_times": potion["brew_times"],
        "base_prices": potion["base_prices"]
    }

def get_cauldron_metadata(key: str) -> dict:
    """
    This function retrieves information about cauldrons that are not stored as part of
    the save data.

    :param key: The internal key used for this item.
    :return:
    """
    cauldron = all_cauldrons[key]
    return {
        "name": cauldron["name"],
        "localization_key": cauldron["secondary_key"],
        "levels": cauldron["levels"]
    }