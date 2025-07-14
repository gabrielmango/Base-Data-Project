from pymongo import MongoClient

from src.utils.base.base_component import BaseComponent


class MongoDBConnection(BaseComponent):
    def __init__(self, connection_string, database_name):
        super().__init__(name=self.__class__.__name__)
        self.connection_string = connection_string
        self.database_name = database_name
        self.client = None
        self.db = None

    def __enter__(self):
        self.logger.info(
            f'Opening connection to MongoDB: {self.database_name}'
        )
        self.client = MongoClient(self.connection_string)
        self.db = self.client[self.database_name]
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()
            self.logger.info('Connection to MongoDB closed.')
