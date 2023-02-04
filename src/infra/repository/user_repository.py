from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.user import User
from collections import namedtuple


class UserRepository:
    @classmethod
    def insert_user(cls, name: str, password: str) -> User:
        insert_data = namedtuple("User", "id name, password")
        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return insert_data(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except Exception as e:
                db_connection.session.rollback()
                print(e)
                raise
            finally:
                db_connection.session.close()
