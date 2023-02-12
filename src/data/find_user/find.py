from typing import Type

from src.data.interfaces.user_repository_interface import UserRepositoryInterface
from src.domain.models.users import UserTuple
from src.domain.use_cases.find_user import FindUserInterface
from src.infra.repository.user_repository import UserRepository


class FindUser(FindUserInterface):
    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository or UserRepository()

    def by_id(self, user_id: int) -> dict[bool, UserTuple]:
        user = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            user = self.user_repository.select_user_by_id(user_id=user_id)
        return {"success": validate_entry, "data": user}

    def by_name(self, name: str) -> dict[bool, list[UserTuple]]:
        user = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            user = self.user_repository.select_user_by_name(name=name)
        return {"success": validate_entry, "data": user}
