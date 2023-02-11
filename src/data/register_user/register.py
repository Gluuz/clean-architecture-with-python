from typing import Type

from src.data.interfaces.user_repository_interface import UserRepositoryInterface
from src.domain.models.users import UserTuple
from src.domain.use_cases.register_user import RegisterUserInterface
from src.infra.repository.user_repository import UserRepository


class RegisterUser(RegisterUserInterface):
    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self._user_repository = user_repository or UserRepository()

    def register(self, name: str, password: str) -> dict[bool, UserTuple]:

        new_user = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            new_user = self._user_repository.insert_user(name=name, password=password)

        return {"success": validate_entry, "data": new_user}
