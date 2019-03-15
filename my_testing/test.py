from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

import pytest

from tests.setup import load_app, cookie_close
from tests.login import login_valid, login_invalid, logout, login_cancel
from tests.find_map import find_map


@pytest.mark.complex
def test_setup(selenium, base_url):
    """Test Suite: 1. Setup application
    """

    load_app(selenium, base_url)
    cookie_close(selenium)


@pytest.mark.complex
def test_login(selenium, base_url, variables):
    """Test Suite: 2. Login
    """

    load_app(selenium, base_url)
    login_invalid(selenium, variables)
    login_cancel(selenium)
    login_valid(selenium, variables)
    logout(selenium)


@pytest.mark.complex
def test_find_map(selenium, base_url, variables):
    """Test Suite: 3. Find map
    """

    load_app(selenium, base_url)
    login_valid(selenium, variables)
    find_map(selenium, variables)