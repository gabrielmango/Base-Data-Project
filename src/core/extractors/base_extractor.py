from abc import ABC, abstractmethod

from src.utils.base.base_component import BaseComponent


class BaseExtractor(BaseComponent, ABC):
    def __init__(self, name=None):
        super().__init__(name=name or self.__class__.__name__)

    @abstractmethod
    def extract(self, *args, **kwargs):
        """Extract data from a source"""
        pass

    def validate_output(self, data):
        """Validate extracted data"""
        if not data:
            self.logger.error('Extraction returned empty data!')
            raise ValueError('Invalid extraction data.')
        self.logger.info(
            f'Data successfully extracted: {type(data).__name__}, {len(data)} records!'
        )
