from src.domain.models.users import user_tuple
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.user import User


class UserRepository:
    @classmethod
    def insert_user(cls, name: str, password: str) -> User:
        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return user_tuple(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except Exception as e:
                db_connection.session.rollback()
                print(e)
                raise
            finally:
                db_connection.session.close()
