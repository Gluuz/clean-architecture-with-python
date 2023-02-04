from faker import Faker

from src.infra.config.db_config import DBConnectionHandler
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
