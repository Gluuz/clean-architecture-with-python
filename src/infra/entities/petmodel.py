from sqlalchemy import Column, String, ForeignKey, Integer, Enum

from src.infra.config.db_base import Base


class AnimalSpecies(Enum):
    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class PetModel(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=False)
    specie = Column(Enum, nullable=False, unique=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __rep__(self):
        return (
            f"Pet: [name={self.name}], Specie: [{self.specie}], Owner: [{self.user_id}]"
        )

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.specie == other.specie
            and self.age == other.age
            and self.user_id == other.user_id
        ):
            return True
        return False
