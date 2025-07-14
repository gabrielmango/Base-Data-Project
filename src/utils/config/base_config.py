import os
import sys
from abc import ABC, abstractmethod

from dotenv import load_dotenv

from src.utils.base.base_component import BaseComponent

load_dotenv()


class BaseConfig(BaseComponent, ABC):
    def __init__(self):
        super().__init__(name=self.__class__.__name__)
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

    def as_dict(self) -> dict:
        return {var: getattr(self, var, None) for var in self.required_vars}
