from abc import ABC, abstractmethod

from src.utils.error_handling import ErrorHandler


class BasePipeline(ABC):
    def __init__(self, name=None):
        self.pipeline_name = name or self.__class__.__name__
        self.error_handler = ErrorHandler(self.pipeline_name)

    @abstractmethod
    def run(self):
        """Main method that must be implemented in subclasses"""
        pass

    def execute(self):
        """Run the pipeline with error handling and logging"""
        return self.error_handler(self.run)()
