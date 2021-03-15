from dataclasses import dataclass
from typing import List

from entity.card import Card


@dataclass
class Deck:
    cards: List[Card]
