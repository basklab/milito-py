from typing import List

from entity.card import UnitCard, LeaderCard, Card
from entity.deck import Deck


def ancient_british():
    unit_specs = []
    unit_specs += 6 * [warband_medium_infantry]
    unit_specs += 6 * [slingers]
    unit_specs += 6 * [chariots]
    unit_specs += 4 * [light_cavalry]
    result: List[Card] = []
    result += leader_cards
    result += [UnitCard(**card.__dict__) for card in unit_specs]
    for i, card in enumerate(result):
        card.idx = i
    return Deck(result)


leader_cards = [
    LeaderCard(
        combat_value=3,
        place_unit_ability=3,
    ),
    LeaderCard(
        combat_value=2,
        place_unit_ability=2,
    ),
    LeaderCard(
        combat_value=2,
        place_unit_ability=1,
        special_effect="if win combat",
    ),
    LeaderCard(
        combat_value=1,
        place_unit_ability=2,
        special_effect="+2 if played in Wood or Rough column.",
    ),
    LeaderCard(
        combat_value=1,
        place_unit_ability=1,
        special_effect="+2 if played with 2x Chariots",
    ),
    LeaderCard(
        combat_value=1,
        place_unit_ability=1,
        special_effect="+2 if played with 2x Slingers",
    ),
    LeaderCard(
        combat_value=1,
        place_unit_ability=1,
        special_effect="+2 if played with 2x Warband Medium Infantry",
    ),
    LeaderCard(
        combat_value=-1,
        place_unit_ability=1,
    ),
]

warband_medium_infantry = UnitCard(
    unit_type="Warband_Med_Inf",
    speed=2,
    attack_strength=4,
    defence_strength=2,
)

slingers = UnitCard(
    unit_type="Slingers",
    speed=3,
    attack_strength=1,
    defence_strength=1,
    combine_ability=True,
)

chariots = UnitCard(
    unit_type="Chariots",
    speed=3,
    attack_strength=4,
    defence_strength=2,
)

light_cavalry = UnitCard(
    unit_type="Light_Cavalry",
    speed=5,
    attack_strength=1,
    defence_strength=1,
)
