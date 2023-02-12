from src.data.interfaces.pet_repository_interface import PetRepositoryInterface
from src.domain.models.pets import PetTuple

fake_user = PetTuple(id=12345, user_id=123, name="jayjay", specie="turtle", age=15)


class PetRepositoryFake(PetRepositoryInterface):
    def __init__(self):
        self.insert_pet_params = {}
        self.select_pet_params = {}

    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> PetTuple:

        self.insert_pet_params["name"] = name
        self.insert_pet_params["specie"] = specie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["user_id"] = user_id

        return fake_user

    def select_pet_by_id(self, pet_id: int = None) -> PetTuple:
        self.select_pet_params["pet_id"] = pet_id

        return fake_user

    def select_pet_by_user_id(self, user_id: int = None) -> list[PetTuple]:
        self.select_pet_params["user_id"] = user_id

        return [fake_user]
