from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine_to_database(self) -> Engine:

        connection_engine = create_engine(self.__connection_string)
        return connection_engine

    def __enter__(self):
        connection_engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=connection_engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
