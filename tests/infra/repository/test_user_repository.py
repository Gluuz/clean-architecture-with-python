from faker import Faker

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.usermodel import UserModel
from src.infra.repository.user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_should_insert_user():
    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine_to_database()

    new_user = user_repository.insert_user(name=name, password=password)
    select_user = engine.execute(
        f"SELECT * FROM users WHERE id={new_user.id}"
    ).fetchone()

    engine.execute(f"DELETE FROM users WHERE id={new_user.id}")

    assert new_user.id == select_user.id
    assert new_user.name == select_user.name
    assert new_user.password == select_user.password


def test_should_select_user_by_id_and_compare_it():
    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()

    fake_user = UserModel(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine_to_database()
    engine.execute(
        f"INSERT INTO users (id, name, password) VALUES ({user_id}, {name}, {password})"
    )

    user = user_repository.select_user_by_id(user_id=user_id)

    assert fake_user in user

    engine.execute(f"DELETE FROM users WHERE id={user_id}")


def test_should_select_user_by_name_and_compare_it():
    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()

    fake_user = UserModel(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine_to_database()
    engine.execute(
        f"INSERT INTO users (id, name, password) VALUES ({user_id}, {name}, {password})"
    )

    user = user_repository.select_user_by_id(name=name)

    assert fake_user in user

    engine.execute(f"DELETE FROM users WHERE id={user_id}")
