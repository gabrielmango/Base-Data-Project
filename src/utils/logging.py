import logging
import os
from datetime import datetime


class Logging:
    _configured = False

    def __init__(self, name):
        self.script_name = os.path.basename(name).replace('.py', '')
        self.log_folder = 'logs'
        self.date_folder = datetime.now().strftime('%Y_%m_%d')
        self.log_file = os.path.join(
            self.log_folder, self.date_folder, f'{self.script_name}.log'
        )

        self.create_logs_folder()

        if not Logging._configured:
            self.configure_logs()
            Logging._configured = True

    def create_logs_folder(self):
        log_dir = os.path.dirname(self.log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def configure_logs(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file, encoding='utf-8'),
                logging.StreamHandler(),
            ],
        )
