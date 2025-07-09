from abc import ABC, abstractmethod

from src.utils.logging import Logging


class BaseExtractor(ABC):
    def __init__(self):
        self.logger = Logging(self.__class__.__name__)

    @abstractmethod
    def extract(self, *args, **kwargs):
        """Extract data from a source"""
        pass

    def validate_output(self, data):
        """Validate extracted data"""
        if not data:
            self.logger.error('Extraction returned empty data')
            raise ValueError('Invalid extraction data')
