from abc import ABC, abstractmethod
from typing import List
from src.domain.models.pets import PetTuple


class PetRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> PetTuple:
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def select_pet_by_id(self, pet_id: int = None) -> PetTuple:
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def select_pet_by_user_id(self, user_id: str = None) -> List[PetTuple]:
        """abstractmethod"""

        raise Exception("Method not implemented")
