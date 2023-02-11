from abc import ABC, abstractmethod
from src.domain.models.users import UserTuple


class UserRepositoryInterface(ABC):
    """Interface to User Repository"""

    @abstractmethod
    def insert_user(self, name: str, password: str) -> UserTuple:
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def select_user_by_id(self, user_id: int = None) -> UserTuple:
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def select_user_by_name(self, name: str = None) -> list[UserTuple]:
        """abstractmethod"""

        raise Exception("Method not implemented")
