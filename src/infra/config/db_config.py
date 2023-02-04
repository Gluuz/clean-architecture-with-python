from sqlalchemy import create_engine, Engine


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine_to_database(self) -> Engine:

        connection_engine = create_engine(self.__connection_string)
        return connection_engine
