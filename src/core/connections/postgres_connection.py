from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from src.utils.logging import Logging


class PostgresConnection:
    def __init__(self, connection_string: str):
        self.logger = Logging(self.__class__.__name__)
        self.connection_string = connection_string
        self.engine = create_engine(self.connection_string)
        self.connection = None

    def __enter__(self):
        self.logger.info('Opening database connection.')
        self.connection = self.engine.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            self.logger.info('Database connection closed.')

    def execute_query(self, query: str) -> list:
        self.logger.info(f'Executing SELECT query: {query}')
        try:
            result = self.connection.execute(text(query))
            columns = result.keys()
            data = [dict(zip(columns, row)) for row in result.fetchall()]
            self.logger.info(f'Query returned {len(data)} rows.')
            return data
        except SQLAlchemyError as e:
            self.logger.error(f'Error executing SELECT query: {e}')
            return []

    def execute_modify(self, query: str):
        self.logger.info(f'Executing modifying query: {query}')
        try:
            with self.engine.begin() as connection:
                connection.execute(text(query))
            self.logger.info('Query executed successfully.')
        except SQLAlchemyError as e:
            self.logger.error(f'Error executing query: {e}')
