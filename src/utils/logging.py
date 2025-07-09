import logging
import os
from datetime import datetime


class Logging:
    def __init__(self, name):
        self.script_name = str(os.path.basename(name)).replace('.py', '')
        self.log_folder = 'logs'
        self.date_folder = str(datetime.now())[:10].replace('-', '_')
        self.log_file = (
            f'{self.log_folder}/{self.date_folder}/{self.script_name}.log'
        )
        self.create_logs_folder()
        self.configure_logs()

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
