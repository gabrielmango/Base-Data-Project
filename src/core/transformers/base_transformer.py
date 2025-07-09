from abc import ABC, abstractmethod

from src.utils.logging import Logging


class BaseTransformer(ABC):
    def __init__(self):
        self.logger = Logging(self.__class__.__name__)

    @abstractmethod
    def transform(self, data, *args, **kwargs):
        """Transform data"""
        pass
