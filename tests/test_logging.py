import os
import shutil

import pytest


@pytest.fixture
def cleanup_logs():
    """Remove the logs folder before and after the test."""
    log_dir = 'logs'
    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)
    yield
    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)
