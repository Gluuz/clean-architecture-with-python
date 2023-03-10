from src.data.interfaces.user_repository_interface import UserRepositoryInterface
from src.domain.models.users import UserTuple
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.usermodel import UserModel


class UserRepository(UserRepositoryInterface):
    @classmethod
    def insert_user(cls, name: str, password: str) -> UserModel:
        with DBConnectionHandler() as db_connection:
            try:
                new_user = UserModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return UserTuple(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except Exception as e:
                db_connection.session.rollback()
                print(e)
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_user_by_id(cls, user_id: int = None) -> list[UserTuple]:
        try:
            with DBConnectionHandler() as db_connection:
                user = (
                    db_connection.session.query(UserModel).filter_by(id=user_id).one()
                )
                return [user]
        except Exception as ex:
            db_connection.session.rollback()
            raise ex
        finally:
            db_connection.session.close()

    @classmethod
    def select_user_by_name(cls, user_name: str = None) -> list[UserTuple]:
        try:
            with DBConnectionHandler() as db_connection:
                user = (
                    db_connection.session.query(UserModel)
                    .filter_by(name=user_name)
                    .one()
                )
                return [user]
        except Exception as ex:
            db_connection.session.rollback()
            raise ex
        finally:
            db_connection.session.close()
