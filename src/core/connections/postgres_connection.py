from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from src.utils.base.base_component import BaseComponent


class PostgresConnection(BaseComponent):
    def __init__(self, connection_string: str):
        super().__init__(name=self.__class__.__name__)
        self.connection_string = connection_string
        self.engine = create_engine(self.connection_string)
        self.connection = None

    def __enter__(self):
        self.logger.info('Opening connection to PostgreSQL.')
        self.connection = self.engine.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            self.logger.info('Connection to PostgreSQL closed.')

    def execute_query(self, query: str) -> list:
        self.logger.info(f'Executing SELECT: {query}')
        try:
            result = self.connection.execute(text(query))
            columns = result.keys()
            data = [dict(zip(columns, row)) for row in result.fetchall()]
            self.logger.info(f'Query returned {len(data)} rows.')
            return data
        except SQLAlchemyError as e:
            self.logger.error(f'Error executing SELECT: {e}', exc_info=True)
            return []

    def execute_modify(self, query: str):
        self.logger.info(f'Performing modification: {query}')
        try:
            with self.engine.begin() as connection:
                connection.execute(text(query))
            self.logger.info('Modification executed successfully.')
        except SQLAlchemyError as e:
            self.logger.error(
                f'Error executing modification: {e}', exc_info=True
            )
