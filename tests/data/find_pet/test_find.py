from src.data.find_pet.find import FindPet
from tests.helpers.repository.pet import PetRepositoryFake


def test_should_find_by_pet_id():

    pet_repo = PetRepositoryFake()
    find_pet = FindPet(pet_repo)

    response = find_pet.by_id(pet_id=12345)

    assert pet_repo.select_pet_params["pet_id"] == 12345

    assert response["success"] is True
    assert response["data"]


def test_should_fail_when_pet_id_is_invalid():

    pet_repo = PetRepositoryFake()
    find_pet = FindPet(pet_repo)

    response = find_pet.by_id(pet_id="should_fail")

    assert pet_repo.select_pet_params == {}

    assert response["success"] is False
    assert response["data"] is None


def test_should_find_pet_by_user_id():
    pet_repo = PetRepositoryFake()
    find_pet = FindPet(pet_repo)

    response = find_pet.by_user_id(user_id=1234)

    assert pet_repo.select_pet_params["user_id"] == 1234

    assert response["success"] is True
    assert response["data"]


def test_should_fail_when_user_id_is_invalid():

    pet_repo = PetRepositoryFake()
    find_pet = FindPet(pet_repo)

    response = find_pet.by_user_id(user_id="should_fail")

    assert pet_repo.select_pet_params == {}

    assert response["success"] is False
    assert response["data"] is None
