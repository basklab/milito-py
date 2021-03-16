from abc import abstractmethod, ABC
from dataclasses import dataclass

from shared.dtos import CardDTO


@dataclass
class Card(ABC):
    idx: int = 0

    @property
    @abstractmethod
    def unit_type(self):
        pass

    def to_dto(self):
        return CardDTO(
            idx=self.idx,
            unit_type=self.unit_type,
        )


@dataclass
class LeaderCard(Card):
    combat_value: int = 0
    place_unit_ability: int = 0
    special_effect: str = ""

    @property
    def unit_type(self):
        return f"leader_{self.idx}"


@dataclass
class UnitCard(Card):
    unit_type: str = ""
    speed: int = 0
    attack_strength: int = 0
    defence_strength: int = 0
    deploy_penalty: int = 0
    flank_penalty: int = 0
    combine_ability: int = 0
    attack_modifiers: int = 0
    defence_modifiers: int = 0
