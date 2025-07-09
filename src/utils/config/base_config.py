import os
import sys
from abc import ABC, abstractmethod

from dotenv import load_dotenv

from utils.logging import Logging

load_dotenv()


class BaseConfig(ABC):
    def __init__(self):
        self.logger = Logging(self.__class__.__name__)
        self._validate()
        self._load()

    @property
    @abstractmethod
    def required_vars(self) -> list[str]:
        pass

    def _validate(self):
        missing = [var for var in self.required_vars if os.getenv(var) is None]
        if missing:
            self.logger.error(
                f"Missing environment variables: {', '.join(missing)}"
            )
            sys.exit(1)

    def _load(self):
        for var in self.required_vars:
            setattr(self, var, os.getenv(var))
            self.logger.info(f'[CONFIG] {var} loaded successfully.')
