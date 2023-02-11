from src.data.interfaces.pet_repository_interface import PetRepositoryInterface
from src.domain.models.pets import PetTuple
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.petmodel import PetModel


class PetRepository(PetRepositoryInterface):
    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> PetTuple:
        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()
                return PetTuple(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                )
            except Exception as ex:
                db_connection.session.rollback()
                raise ex
            finally:
                db_connection.session.close()

    @classmethod
    def select_pet_by_id(cls, pet_id: int = None) -> PetTuple:
        try:
            with DBConnectionHandler() as db_connection:
                selected_pet = (
                    db_connection.session.query(PetModel).filter_by(pet_id=pet_id).one()
                )
                return selected_pet
        except Exception as ex:
            db_connection.session.rollback()
            raise ex
        finally:
            db_connection.session.close()

    @classmethod
    def select_pet_by_user_id(cls, user_id: str = None) -> list[PetTuple]:
        try:
            with DBConnectionHandler() as db_connection:
                selected_pets = (
                    db_connection.session.query(PetModel)
                    .filter_by(user_id=user_id)
                    .all()
                )
                return [selected_pets]
        except Exception as ex:
            db_connection.session.rollback()
            raise ex
        finally:
            db_connection.session.close()
