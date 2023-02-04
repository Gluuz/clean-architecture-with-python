from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.infra.config.db_base import Base


class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=False)
    id_pet = relationship("Pets")

    def __rep__(self):
        return f"User {self.name}"
