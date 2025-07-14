import logging
from datetime import datetime
from functools import wraps


class ErrorHandler:
    def __init__(self, logger_name=None):
        self.logger = (
            logging.getLogger(logger_name)
            if logger_name
            else logging.getLogger(__name__)
        )

    def __call__(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            return self.execute(func, *args, **kwargs)

        return wrapped

    def execute(self, func, *args, **kwargs):
        self.logger.info(f'Starting process!')
        start_time = datetime.now()

        try:
            result = func(*args, **kwargs)
            self.logger.info(f'Completed successfully')
            return result
        except Exception as e:
            self.logger.error(f'{str(e)}', exc_info=True)
            raise
        finally:
            end_time = datetime.now()
            duration = end_time - start_time
            self.logger.info(
                f'Execution time: {duration.total_seconds():.4f} seconds'
            )
            self.logger.info('─' * 60)
