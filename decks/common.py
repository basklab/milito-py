from entity.card import UnitCard
import random

from entity.deck import Deck

light_cavalry = UnitCard(
    unit_type="Light_Cavalry",
    speed=5,
    attack_strength=1,
    defence_strength=1,
)


slingers = UnitCard(
    unit_type="Slingers",
    speed=3,
    attack_strength=1,
    defence_strength=1,
    combine_ability=True,
)
