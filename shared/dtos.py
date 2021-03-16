from dataclasses import dataclass
from typing import List

from shared.enums import PhasesEnum, FactionsEnum


class DTO:
    pass


@dataclass
class CardDTO(DTO):
    idx: int
    unit_type: str


@dataclass
class DeckDTO(DTO):
    cards: List[CardDTO]


@dataclass
class HandDTO(DTO):
    cards: List[CardDTO]


@dataclass
class PlayerInfoDTO(DTO):
    hand: HandDTO
    playerId: int
    faction: FactionsEnum
    row1: List[CardDTO]
    row2: List[CardDTO]


@dataclass
class GameTableDTO(DTO):
    neutral: List[int]
    phase: PhasesEnum
    currentPlayer: PlayerInfoDTO
    anotherPlayer: PlayerInfoDTO
