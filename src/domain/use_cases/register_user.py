from abc import ABC, abstractmethod

from src.domain.models.users import UserTuple


class RegisterUserInterface(ABC):
    @abstractmethod
    def register(cls, name: str, password: str) -> dict[bool, UserTuple]:
        raise Exception("Should implement method: register")
