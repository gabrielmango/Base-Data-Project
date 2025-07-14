from abc import ABC, abstractmethod

from src.utils.base.base_component import BaseComponent


class BaseLoader(BaseComponent, ABC):
    def __init__(self, name=None):
        super().__init__(name=name or self.__class__.__name__)

    @abstractmethod
    def load(self, data, *args, **kwargs):
        """Load data to a destination"""
        pass
