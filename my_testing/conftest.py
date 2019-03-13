import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


SELENIUM=None
DONT_QUIT=False


@pytest.fixture
def selenium(selenium, stop):

    # selenium.implicitly_wait(2)

    selenium.set_window_size(1440, 810)
    # selenium.maximize_window()

    global DONT_QUIT
    DONT_QUIT = stop

    global SELENIUM
    SELENIUM = selenium

    yield selenium


def pytest_addoption(parser):

    parser.addoption('--stop', action="store_true",
        help="Keep web browser opened if test failed.")


def pytest_report_teststatus (report):
    global SELENIUM
    global DONT_QUIT

    def empty_function():
        """Just empty method, do nothing"""
        pass

    # we only look at actual failing test calls, not setup/teardown
    if (report.outcome == 'failed' or report.failed) and DONT_QUIT:
        SELENIUM.quit = empty_function


@pytest.fixture
def stop(request):
    return request.config.getoption("--stop")
