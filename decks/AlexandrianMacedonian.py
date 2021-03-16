from decks.common import light_cavalry, slingers
from entity.card import UnitCard, LeaderCard
from entity.deck import Deck


def alexandrian_macedonian():
    unit_specs = []
    unit_specs += 7 * [pikes]
    unit_specs += 4 * [spears]
    unit_specs += 3 * [light_infantry]
    unit_specs += 2 * [slingers]
    unit_specs += 2 * [companions]
    unit_specs += 2 * [heavy_cavalry]
    unit_specs += 2 * [light_cavalry]
    unit_cards = [UnitCard(**card.__dict__) for card in unit_specs]
    return Deck.make(leader_cards=leader_cards, unit_cards=unit_cards)


leader_cards = [
    LeaderCard(
        combat_value=3,
        place_unit_ability=3,
    ),
    LeaderCard(
        combat_value=2,
        place_unit_ability=3,
    ),
    LeaderCard(
        combat_value=2,
        place_unit_ability=2,
        special_effect="if combat is tied...",
    ),
    LeaderCard(
        combat_value=2,
        place_unit_ability=2,
        special_effect="+1 if attacking",
    ),
    LeaderCard(
        combat_value=2,
        place_unit_ability=2,
    ),
    LeaderCard(
        combat_value=1,
        place_unit_ability=2,
        special_effect="+2 if played with Pikes",
    ),
    LeaderCard(
        combat_value=1,
        place_unit_ability=2,
        special_effect="+2 if played with Compamnions",
    ),
    LeaderCard(
        combat_value=-1,
        place_unit_ability=1,
    ),
]

pikes = UnitCard(
    unit_type="Pikes",
    speed=0,
    attack_strength=5,
    defence_strength=5,
    deploy_penalty=2,
    flank_penalty=1,
)

spears = UnitCard(
    unit_type="Spears",
    speed=0,
    attack_strength=4,
    defence_strength=5,
    deploy_penalty=1,
    flank_penalty=1,
)

light_infantry = UnitCard(
    unit_type="Light_Infantry",
    speed=3,
    attack_strength=2,
    defence_strength=2,
    combine_ability=True,
)

companions = UnitCard(
    unit_type="Companions",
    speed=3,
    attack_strength=4,
    defence_strength=2,
)

heavy_cavalry = UnitCard(
    unit_type="Heavy_Cavalry",
    speed=3,
    attack_strength=4,
    defence_strength=3,
    deploy_penalty=1,
    flank_penalty=1,
)
