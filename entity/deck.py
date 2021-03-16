import random
from dataclasses import dataclass
from typing import List

from entity.card import Card
from shared.dtos import HandDTO, DeckDTO


@dataclass
class Deck:
    cards: List[Card]

    @staticmethod
    def make(leader_cards, unit_cards):
        result = leader_cards + unit_cards
        for i, card in enumerate(result):
            card.idx = i
        random.seed(42)
        random.shuffle(result)
        return Deck(result)

    def to_dto(self):
        return DeckDTO(
            cards=[card.to_dto() for card in self.cards]
        )


class Hand(Deck):

    def to_dto(self):
        return HandDTO(**self.__dict__)
