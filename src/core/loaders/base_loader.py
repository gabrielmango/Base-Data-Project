from abc import ABC, abstractmethod

from src.utils.logging import Logging


class BaseLoader(ABC):
    def __init__(self):
        self.logger = Logging(self.__class__.__name__)

    @abstractmethod
    def load(self, data, *args, **kwargs):
        """Load data to a destination"""
        pass
