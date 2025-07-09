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
        func_name = func.__name__
        class_name = args[0].__class__.__name__ if args else 'Module'
        full_name = (
            f'{class_name}.{func_name}'
            if class_name != 'Module'
            else func_name
        )

        self.logger.info(f'🚀 Starting process: {full_name}')
        start_time = datetime.now()

        try:
            result = func(*args, **kwargs)
            self.logger.info(f'✅ {full_name} completed successfully')
            return result
        except Exception as e:
            self.logger.error(
                f'❌ ERROR in {full_name}: {str(e)}', exc_info=True
            )
            raise
        finally:
            end_time = datetime.now()
            duration = end_time - start_time
            self.logger.info(
                f'⏱️ Execution time: {duration.total_seconds():.2f} seconds'
            )
            self.logger.info('─' * 60)
