from abc import ABC, abstractmethod

from src.domain.models.users import UserTuple


class FindUserInterface(ABC):
    @abstractmethod
    def by_id(self, user_id: int) -> dict[bool, UserTuple]:

        raise Exception("Should implement method: find_user_by_id")

    @abstractmethod
    def by_name(self, name: str) -> dict[bool, list[UserTuple]]:
        raise Exception("Should implement method: find_user_by_name")
