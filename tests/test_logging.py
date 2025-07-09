import os
import shutil
from datetime import datetime

import pytest

from src.utils.logging import Logging


@pytest.fixture
def cleanup_logs():
    """Remove the logs folder before and after the test."""
    log_dir = 'logs'
    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)
    yield
    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)


def test_log_directory_and_file_creation(cleanup_logs):
    logger = Logging('teste_script.py')
    expected_dir = f'logs/{datetime.now().strftime("%Y_%m_%d")}'
    expected_file = f'{expected_dir}/teste_script.log'

    assert os.path.isdir(expected_dir), 'Logs directory not created!'
    assert os.path.isfile(expected_file), 'Log file not created!'
