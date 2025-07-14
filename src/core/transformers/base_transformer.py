from abc import ABC, abstractmethod

from src.utils.base.base_component import BaseComponent


class BaseTransformer(BaseComponent, ABC):
    def __init__(self, name=None):
        super().__init__(name=name or self.__class__.__name__)

    @abstractmethod
    def transform(self, data, *args, **kwargs):
        """Transform data"""
        pass
