from src.data.interfaces.user_repository_interface import UserRepositoryInterface
from src.domain.models.users import UserTuple

fake_user = UserTuple(id=1000, name="fake_name", password="fake_password")


class UserRepositoryFake(UserRepositoryInterface):
    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(self, name: str, password: str) -> UserTuple:

        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password

        return fake_user

    def select_user_by_id(self, user_id: int = None) -> UserTuple:
        self.select_user_params["user_id"] = user_id

        return fake_user

    def select_user_by_name(self, name: str = None) -> list[UserTuple]:
        self.select_user_params["name"] = name

        return [fake_user]
