from framework.configure import get_config_path
import os


def test_file_open():
    assert os.path.exists(get_config_path()) is True
