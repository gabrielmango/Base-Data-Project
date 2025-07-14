from abc import ABC, abstractmethod

from src.utils.base.base_component import BaseComponent


class BasePipeline(BaseComponent, ABC):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.pipeline_name = self.component_name

    @abstractmethod
    def run(self):
        """Main method that must be implemented in subclasses"""
        pass

    def execute(self):
        """Run the pipeline with error handling and logging"""
        self.logger.info(f'Running pipeline: {self.pipeline_name}')
        return self.error_handler(self.run)()
