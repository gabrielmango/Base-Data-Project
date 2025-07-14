import logging
from abc import ABC

from src.utils.error_handling import ErrorHandler
from src.utils.logging import Logging


class BaseComponent(ABC):
    def __init__(self, name=None):
        self.component_name = name or self.__class__.__name__

        self.logger_config = Logging(name=self.component_name)
        self.logger = logging.getLogger(self.component_name)

        self.error_handler = ErrorHandler(logger_name=self.component_name)
