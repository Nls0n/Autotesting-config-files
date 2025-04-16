import pytest
from framework.configure import get_config_path
from framework.configure import parse_file


@pytest.fixture
def config():
    config_path = get_config_path()
    return parse_file(config_path)


@pytest.fixture
def sections() -> dict:
    data = parse_file()
    return data
