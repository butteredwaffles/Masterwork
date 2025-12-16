meta:
  id: potionomics
  title: Potionomics Save Data
  endian: le
seq:
  - id: world
    type: world_state
  - id: len_ingredients
    type: u4
  - id: ingredients
    type: ingredient_with_quantity
    repeat: expr
    repeat-expr: len_ingredients
  - id: len_potions
    type: u4
  - id: potions
    type: potion_with_quantity
    repeat: expr
    repeat-expr: len_potions
  - id: len_fuel
    type: u4
  - id: fuel
    type: fuel_with_quantity
    repeat: expr
    repeat-expr: len_fuel
  - id: len_event_flags
    type: u4
  - id: event_flags
    type: event_flag
    repeat: expr
    repeat-expr: len_event_flags
  - id: len_progress_flags
    type: u4
  - id: progress_flags
    type: progress_flag
    repeat: expr
    repeat-expr: len_progress_flags
  - id: len_completed_chapters
    type: u4
  - id: completed_chapters
    type: str_with_len
    repeat: expr
    repeat-expr: len_completed_chapters
  - id: len_stucco_walls
    type: u4
  - id: stucco_walls
    type: str_with_len
    repeat: expr
    repeat-expr: len_stucco_walls
  - id: len_wood_walls
    type: u4
  - id: wood_walls
    type: str_with_len
    repeat: expr
    repeat-expr: len_wood_walls
  - id: len_floors
    type: u4
  - id: floors
    type: str_with_len
    repeat: expr
    repeat-expr: len_floors
  - id: len_inventory_display_shelves
    type: u4
  - id: inventory_display_shelves
    type: shelf
    repeat: expr
    repeat-expr: len_inventory_display_shelves
  - id: len_inventory_shop_shelves
    type: u4
  - id: inventory_shop_shelves
    type: shelf
    repeat: expr
    repeat-expr: len_inventory_shop_shelves
  - id: len_inventory_cauldrons
    type: u4
  - id: inventory_cauldrons
    type: cauldron
    repeat: expr
    repeat-expr: len_inventory_cauldrons
  - id: len_inventory_aging_barrels
    type: u4
  - id: inventory_aging_barrels
    type: aging_barrel
    repeat: expr
    repeat-expr: len_inventory_aging_barrels
  - id: len_past_events
    type: u4
  - id: past_events
    type: event
    repeat: expr
    repeat-expr: len_past_events
  - id: len_unlocked_cards
    type: u4
  - id: unlocked_cards
    type: str_with_len
    repeat: expr
    repeat-expr: len_unlocked_cards
  - id: len_slime_bulbs
    type: u4
  - id: slime_bulbs
    type: slime_bulb
    repeat: expr
    repeat-expr: len_slime_bulbs
  - id: len_heroes
    type: u4
  - id: heroes
    type: hero
    repeat: expr
    repeat-expr: len_heroes
  - id: len_daily_stats
    type: u4
  - id: daily_stats
    type: daily_stats
    repeat: expr
    repeat-expr: len_daily_stats
  # Not totally sure what this is, but given placement it is likely three int32s
  # for shop front level, shop back level, and shop basement level
  - size: 12
  - id: len_active_cauldrons
    type: u4
  - id: active_cauldrons
    type: cauldron
    repeat: expr
    repeat-expr: len_active_cauldrons
  - id: len_inactive_cauldrons
    type: u4
  - id: inactive_cauldrons
    type: cauldron
    repeat: expr
    repeat-expr: len_inactive_cauldrons
  - id: len_active_aging_barrels
    type: u4
  - id: active_aging_barrels
    type: aging_barrel
    repeat: expr
    repeat-expr: len_active_aging_barrels
  - id: len_active_display_shelves
    type: u4
  - id: active_display_shelves
    type: shelf
    repeat: expr
    repeat-expr: len_active_display_shelves
  - id: len_active_shop_shelves
    type: u4
  - id: active_shop_shelves
    type: shelf
    repeat: expr
    repeat-expr: len_active_shop_shelves
  - id: active_glamours
    type: str_with_len
    repeat: expr
    repeat-expr: 4
  # Around this area there are also booleans for BoughtMarketingPlan, int32 for enchantmentpurchasedate, and bought saltnpepper treasure
  - size: 4
  - id: len_friends
    type: u4
  - id: friends
    type: friend
    repeat: expr
    repeat-expr: len_friends
  - id: len_romances
    type: u4
  - id: romances
    type: str_with_len
    repeat: expr
    repeat-expr: len_romances
  - id: len_hangouts
    type: u4
  - id: hangouts
    type: str_with_len
    repeat: expr
    repeat-expr: len_hangouts
  - id: len_gifts_given
    type: u4
  - id: gifts_given
    type: str_with_len
    repeat: expr
    repeat-expr: len_gifts_given
#  - id: boss_finn_indicator
#    type: u4
#    consume: false
#  - size: 4
#    if: boss_finn_indicator == 0
  - id: len_quinn_unlocks
    type: u4
  - id: quinn_unlocks
    type: str_with_len
    repeat: expr
    repeat-expr: len_quinn_unlocks
  - id: len_quinn_shop_items
    type: u4
  - id: quinn_shop_items
    type: ingredient_with_quantity
    repeat: expr
    repeat-expr: len_quinn_shop_items
  - id: ingredient_types_to_sell
    type: s4
  - id: ingredients_fed
    type: s4
  - size: 4
  - id: purchased_enchantment_today
    type: u4
  - id: active_enchantment
    type: roxanne_enchantment_data
  - size: 4
  - id: len_roxanne_shop_enchantments
    type: u4
  - id: roxanne_shop_enchantments
    type: roxanne_enchantment_data
    repeat: expr
    repeat-expr: len_roxanne_shop_enchantments
  - id: len_saffron_shop_fuel
    type: u4
  - id: saffron_shop_fuel
    type: fuel_with_quantity
    repeat: expr
    repeat-expr: len_saffron_shop_fuel
  - size: 4
  - id: len_active_daily_events
    type: u4
  - id: active_daily_events
    type: event
    repeat: expr
    repeat-expr: len_active_daily_events
  - id: vendor_active_events
    type: event
    repeat: eos

types:
  str_with_len:
    seq:
      - id: len_data
        type: u4
      - id: data
        type: str
        encoding: UTF-8
        size: len_data
  world_state:
    seq:
      - id: day
        type: s4
      - id: time_segment
        type: s4
      - id: time_of_day
        type: u1
        enum: time_of_day
      - id: location
        type: u1
        enum: location
      - id: weather
        type: u1
        enum: weather
      - id: gold
        type: s4
      # May be some weirdness with TEnumAsByte here? This may indicate the tutorial stage
      - type: u4
      # Not terribly confident - needs to be confirmed
      - id: number_of_potions_brewed
        type: s4
      - id: stress
        type: s4
      - id: active_chapter
        type: u4
  loc_table:
    seq:
      - type: u4
      - id: valid
        type: u1
      - size: 4
        if: valid == 0xff
      - id: path
        type: str_with_len
        if: valid != 0xff
      - id: identifier
        type: str_with_len
        if: valid != 0xff
  magimin:
    seq:
      - id: type
        type: u1
        enum: element
      - id: quantity
        type: u4
  traits:
    seq:
      - id: taste
        type: u1
        enum: taste_trait
      - id: sensation
        type: u1
        enum: sensation_trait
      - id: aroma
        type: u1
        enum: aroma_trait
      - id: visual
        type: u1
        enum: visual_trait
      - id: sound
        type: u1
        enum: sound_trait
  ingredient:
    seq:
      - id: name
        type: str_with_len
      - id: localized_name
        type: loc_table
      - id: localized_description
        type: loc_table
      - id: volume
        type: s4
      - id: len_biomes
        type: u4
      - id: biomes
        type: u1
        repeat: expr
        repeat-expr: len_biomes
        enum: biome
      - id: category
        type: u1
        enum: ingredient_category
      - id: len_magimins
        type: u4
      - id: magimins
        type: magimin
        repeat: expr
        repeat-expr: len_magimins
      - id: traits
        type: traits
      - id: len_tags
        type: u4
      - id: tags
        type: str_with_len
        repeat: expr
        repeat-expr: len_tags
  ingredient_with_quantity:
    seq:
      - id: ingredient
        type: ingredient
      - id: quantity
        type: u4
  potion:
    seq:
      - id: name
        type: str_with_len
      - id: localized_name
        type: loc_table
      - id: localized_description
        type: loc_table
      - id: category
        type: u1
        enum: potion_category
      - id: traits
        type: traits
      - id: rank
        type: u1
        enum: potion_rank
      - id: tier
        type: s4
        enum: potion_tier
      - id: star_rating
        type: s4
      - id: effect
        type: u1
        enum: potion_effect
      - id: adventuring_effect_value
        type: s4
      - id: adventure_effects_stack
        type: s4
      - id: was_barrel_aged
        type: s4
      - id: barrel_key
        type: str_with_len
      - id: aging_multiplier
        type: f4
  potion_with_quantity:
    seq:
      - id: potion
        type: potion
      - id: quantity
        type: s4
  fuel:
    seq:
      - id: localized_name
        type: loc_table
      - id: localized_description
        type: loc_table
      - id: time_segments_reduced
        type: s4
      - id: price
        type: s4
  fuel_with_quantity:
    seq:
      - id: fuel
        type: fuel
      - id: quantity
        type: s4
  event_flag:
    seq:
      - id: name
        type: str_with_len
      - id: day_occurred
        type: s4
      - id: time_segment
        type: s4
      - id: time_of_day
        type: u1
        enum: time_of_day
      - id: location
        type: u1
        enum: location
      - id: weather
        type: u1
        enum: weather
  progress_flag:
    seq:
      - id: name
        type: str_with_len
      - id: value
        type: u4
  shelf:
    seq:
      - id: level
        type: s4
      - id: name
        type: str_with_len
      - id: len_potions
        type: u4
      - id: potions
        type: potion
        repeat: expr
        repeat-expr: len_potions
  xy_pair:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
  cauldron:
    seq:
      - id: level
        type: s4
      - id: name
        type: str_with_len
      - id: actively_brewing
        type: u4
      - id: day_obtained
        type: s4
      - id: time_segment_obtained
        type: s4
      - id: time_segments_to_brew
        type: s4
      - id: potion
        type: potion_with_quantity
      - id: len_ingredients
        type: u4
      - id: ingredients
        type: ingredient
        repeat: expr
        repeat-expr: len_ingredients
      - id: len_fuel
        type: u4
      - id: fuel
        type: fuel
        repeat: expr
        repeat-expr: len_fuel
      - id: brew_state
        type: u1
        enum: cauldron_brew_state
      - id: len_ingredient_placements
        type: u4
      - id: ingredient_placements
        type: xy_pair
        repeat: expr
        repeat-expr: len_ingredient_placements
      - id: stability
        type: u1
        enum: cauldron_stability
  aging_barrel:
    seq:
      - id: name
        type: str_with_len
      - id: level
        type: s4
      - id: state
        type: u1
        enum: aging_barrel_state
      - id: day_obtained
        type: s4
      - id: time_segment_obtained
        type: s4
      - id: time_segments_to_age
        type: s4
      - id: potion
        type: potion_with_quantity
      - id: len_potion_placements
        type: u4
      - id: potion_placements
        type: xy_pair
        repeat: expr
        repeat-expr: len_potion_placements
  event_outcome:
    seq:
      - id: type
        type: u1
        enum: event_outcome_type
      - id: len_args
        type: u4
      - id: args
        type: str_with_len
        repeat: expr
        repeat-expr: len_args
  event:
    seq:
      - id: name
        type: str_with_len
      - id: type
        type: u1
        enum: active_event_type
      - id: day_occurred
        type: s4
      - id: duration
        type: s4
      - id: len_outcomes
        type: u4
      - id: outcomes
        type: event_outcome
        repeat: expr
        repeat-expr: len_outcomes
  slime_bulb:
    seq:
      - id: state
        type: u1
        enum: slime_bulb_state
      - id: seed_ingredient
        type: ingredient_with_quantity
      - id: time_slots_remaining
        type: s4
      - id: magimins_used
        type: s4
      - id: previous_ingredient_count
        type: s4
      - id: current_ingredient_count
        type: s4
  reward:
    seq:
      - id: type
        type: u1
        enum: adventure_loot_type
      - id: name
        type: str_with_len
      - id: quantity
        type: s4
      - id: drop_weight
        type: s4
      - id: len_potion_effects
        type: u4
      - id: potion_effects
        type: u1
        enum: potion_effect
        repeat: expr
        repeat-expr: len_potion_effects
  active_hero_potion_effect:
    seq:
      - id: effect
        type: u1
        enum: potion_effect
      - id: value
        type: s4
  hero:
    seq:
      - id: name_key
        type: str_with_len
      - id: name
        type: str_with_len
      - id: level
        type: s4
      - id: experience
        type: s4
      - id: is_on_adventure
        type: u4
      - id: starting_day
        type: s4
      - id: starting_time_segment
        type: s4
      - id: time_segments_until_return
        type: s4
      - id: xp_to_gain
        type: s4
      - id: len_rewards
        type: u4
      - id: rewards
        type: reward
        repeat: expr
        repeat-expr: len_rewards
      - id: adventure_result
        type: str_with_len
      - id: len_equipped_potions
        type: u4
      - id: equipped_potions
        type: potion
        repeat: expr
        repeat-expr: len_equipped_potions
      - id: len_equipped_potion_effects
        type: u4
      - id: equipped_potion_effects
        type: active_hero_potion_effect
        repeat: expr
        repeat-expr: len_equipped_potion_effects
  friend:
    seq:
      - id: name
        type: str_with_len
      - id: level
        type: s4
      - id: current_friendship_points
        type: s4
      - id: flirt_level
        type: s4
      - id: hangout_level
        type: s4
      - id: len_coupons
        type: s4
      - id: coupons
        type: str_with_len
        repeat: expr
        repeat-expr: len_coupons
  roxanne_enchantment_data:
    seq:
      - id: localized_name
        type: loc_table
      - id: localized_description
        type: loc_table
      - id: duration
        type: s4
      - id: cost
        type: s4
      - id: traits
        type: traits
  daily_stats:
    seq:
      - id: number_of_customers
        type: s4
      - id: potions_sold
        type: s4
      - id: gold_spent
        type: s4
      - id: gold_earned
        type: s4
enums:
  time_of_day:
    0: start_of_day
    1: morning
    2: afternoon
    3: night
    4: end_of_day
    5: invalid
  location:
    0: sylvia_shop
    1: counter
    2: cauldron
    3: overworld
    4: quinn_shop
    5: muktuk_shop
    6: saffron_shop
    7: saltnpepper_shop
    8: roxanne
    9: baptiste_guild
    10: luna_shop
    11: carnival
    12: sylvia_basement
    13: dialogue
    14: mint_guild
    15: corsac_guild
    16: xid_guild
    17: sylvia_shop_intro
    18: carnival_final
    19: sylvia_shop_nighttime
    20: gardening
    21: title
    22: credits
  weather:
    0: sunny
    1: cloudy
    2: partly_cloudy
    3: rainy
    4: snowy
    5: sleeting
    6: stormy
    7: lightning
    8: thunder
    9: hailing
    10: windy
    11: foggy
    12: icy
    13: clear_sky
  biome:
    0: no_value
    1: enchanted_forest
    2: mushroom_mire
    3: bone_wastes
    4: storm_plains
    5: the_ocean_coasts
    6: the_shadow_steppe
    7: sulfuric_falls
    8: crystaline_forest
    9: ice_craggs
    10: crater
    11: dragon_oasis
    12: the_artic # typo in the game
    13: magic_wasteland
  ingredient_category:
    0: slime
    1: plant
    2: flower
    3: fruit
    4: fungus
    5: bug
    6: fish
    7: flesh
    8: bone
    9: mineral
    10: essences
    11: gem
    12: ores
    13: pure_mana
    14: ingredientcategory_max
  element:
    0: red
    1: green
    2: yellow
    3: blue
    4: purple
  aroma_trait:
    0: no_value
    1: aromatic
    2: perfumy
    3: floral
    4: citrusy
    5: acris
    6: fetid
    7: noxious
    8: musty
  sensation_trait:
    0: no_value
    1: cool
    2: warm
    3: bubbly
    4: velvety
    5: curdled
    6: greasy
    7: chalky
    8: stringy
  sound_trait:
    0: no_value
    1: murmuring
    2: rustling
    3: fizzing
    4: purring
    5: gurgling
    6: noisy
    7: grating
    8: discordant
  visual_trait:
    0: no_value
    1: sparkling
    2: colorful
    3: shimmering
    4: appetizing
    5: dull
    6: cloudy
    7: viscous
    8: moldy
  taste_trait:
    0: no_value
    1: sweet
    2: savory
    3: spicy
    4: tangy
    5: bitter
    6: sour
    7: astringent
    8: bland
  potion_category:
    0: potions
    1: tonics
    2: enhancers
    3: cures
  potion_rank:
    0: unranked
    1: common
    2: uncommon
    3: rare
  potion_effect:
    0: health
    1: mana
    2: stamina
    3: drowsy
    4: fire_resistance
    5: ice_resistance
    6: radiation_resistance
    7: poison_resistance
    8: sight
    9: silence
    10: speed
    11: thunder_resistance
    12: tolerance
    13: petrification
    14: alertness
    15: curse_resistance
    16: insight
    17: seeker
    18: shadow_resistance
    19: dowsing
  potion_tier:
    0: minor
    1: common
    2: greater
    3: grand
    4: superior
    5: masterwork
  cauldron_brew_state:
    0: add_ingredients
    1: brewing
    2: brew_complete
  cauldron_stability:
    0: too_unstable
    1: unstable
    2: stable
    3: very_stable
    4: perfect
  aging_barrel_state:
    0: add_potion
    1: aging
    2: age_complete
  event_outcome_type:
    0: no_value
    1: increase_ingredient_value
    2: decrease_ingredient_value
    3: increase_ingredient_value_by_category
    4: decrease_ingredient_value_by_category
    5: increase_ingredient_value_by_biome
    6: decrease_ingredient_value_by_biome
    7: increase_potion_value
    8: decrease_potion_value
    9: increase_potion_value_by_category
    10: decrease_potion_value_by_category
    11: increase_potion_trait_value
    12: decrease_potion_trait_value
    13: increase_number_of_customers
    14: decrease_number_of_customers
    15: increase_customer_frequency_by
    16: increase_customer_frequency_by_personality
    17: debuff_customer
    18: biome_supply_up
    19: biome_supply_down
    20: biome_raid
    21: lock_biome
    22: increase_ingredient_supply
    23: decrease_ingredient_supply
    24: increase_ingredient_supply_by_category
    25: decrease_ingredient_supply_by_category
    26: increase_ingredient_supply_by_biome
    27: decrease_ingredient_supply_by_biome
    28: increase_fuel_supply
    29: decrease_fuel_supply
    30: double_relationship_gains
    31: potion_category_patent
  active_event_type:
    0: daily
    1: luna_marketing_plan
    2: baptiste_investment
  slime_bulb_state:
    0: idle
    1: growing
    2: ready_to_harvest
  adventure_loot_type:
    0: ingredient
    1: fuel
    2: floor
    3: wall