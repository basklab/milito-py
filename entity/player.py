from dataclasses import dataclass
from typing import List

from entity.card import UnitCard, Card
from entity.deck import Deck, Hand
from shared.dtos import PlayerInfoDTO, GameTableDTO
from shared.enums import PhasesEnum, FactionsEnum


@dataclass
class SquadFormation:
    main_unit: UnitCard
    support_unit: UnitCard
    bonus_card: Card


@dataclass
class AttackState:
    squad_formation: SquadFormation
    attack_column: int
    defence_column: int


@dataclass
class PlayerState:
    deck: Deck
    dead_pile: Deck
    discard_pile: Deck
    faction: FactionsEnum
    hand: Hand
    player_id: int
    row_1: List[int]
    row_2: List[int]
    state: PhasesEnum

    def to_dto(self):
        return PlayerInfoDTO(**self.__dict__)


@dataclass
class GameState:
    neutral: List[int]
    phase: PhasesEnum
    current_player: PlayerState
    another_player: PlayerState
    battle_state: AttackState

    def to_dto(self):
        return GameTableDTO(**self.__dict__)
