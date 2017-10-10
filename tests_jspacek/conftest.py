import pytest

@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium