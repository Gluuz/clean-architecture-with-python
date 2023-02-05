from faker import Faker

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.petmodel import PetModel
from src.infra.repository.pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection = DBConnectionHandler()


def test_should_insert_pet():
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=3)

    engine = db_connection.get_engine_to_database()

    new_pet = pet_repository.insert_pet(
        name=name, specie=specie, age=age, user_id=user_id
    )

    select_pet = engine.execute(f"SELECT * FROM pets WHERE id={new_pet.id}").fetchone()

    engine.execute(f"DELETE FROM pets WHERE id={new_pet.id}")

    assert new_pet.id == select_pet.id
    assert new_pet.name == select_pet.name
    assert new_pet.age == select_pet.age
    assert new_pet.specie == select_pet.specie
    assert new_pet.user_id == select_pet.user_id


def test_should_select_pet_by_id_and_compare_it():
    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=3)

    new_pet = PetModel(
        pet_id=pet_id, name=name, specie=specie, age=age, user_id=user_id
    )

    engine = db_connection.get_engine_to_database()

    engine.execute(
        f"INSERT INTO pets (id, name, specie, age, user_id) "
        f"VALUES ({pet_id}, {name},{ specie}, {age}, {user_id})"
    )

    select_pet = pet_repository.select_pet_by_id(pet_id=pet_id)

    assert new_pet in select_pet

    engine.execute(f"DELETE FROM pets WHERE id={new_pet.id}")


def test_should_select_pet_by_user_id_and_compare_it():
    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=3)

    new_pet = PetModel(
        pet_id=pet_id, name=name, specie=specie, age=age, user_id=user_id
    )

    engine = db_connection.get_engine_to_database()

    engine.execute(
        f"INSERT INTO pets (id, name, specie, age, user_id) "
        f"VALUES ({pet_id}, {name},{specie}, {age}, {user_id})"
    )

    select_pet = pet_repository.select_pet_by_user_id(user_id=user_id)

    assert new_pet in select_pet

    engine.execute(f"DELETE FROM pets WHERE id={new_pet.id}")
