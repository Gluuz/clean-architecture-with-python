from abc import ABC, abstractmethod

from src.domain.models.pets import PetTuple


class FindPetInterface(ABC):
    @abstractmethod
    def by_id(self, pet_id: int) -> dict[bool, PetTuple]:

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def by_user_id(self, user_id: int) -> dict[bool, list[PetTuple]]:

        raise Exception("Should implement method: by_user_id")
