from typing import Type

from src.data.interfaces.user_repository_interface import UserRepositoryInterface
from src.domain.models.pets import PetTuple
from src.domain.use_cases.find_pet import FindPetInterface
from src.infra.repository.pet_repository import PetRepository


class FindPet(FindPetInterface):
    def __init__(self, pet_repository: Type[UserRepositoryInterface]):
        self.pet_repository = pet_repository or PetRepository()

    def by_id(self, pet_id: int) -> dict[bool, PetTuple]:
        pet = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            pet = self.pet_repository.select_pet_by_id(pet_id=pet_id)
        return {"success": validate_entry, "data": pet}

    def by_user_id(self, user_id: int) -> dict[bool, list[PetTuple]]:
        pets = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            pets = self.pet_repository.select_pet_by_user_id(user_id=user_id)
        return {"success": validate_entry, "data": pets}
