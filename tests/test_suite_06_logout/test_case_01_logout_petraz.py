from test_valid_login import test as case_06_01_02
import pytest
from selenium.webdriver.support.ui import WebDriverWait

def test(selenium, base_url, variables):
    # step_01_open_page
    # step_02_login
    case_06_01_02(selenium, base_url, variables)
    step_03_click_on_logout(selenium)
    verify_logout

def step_03_click_on_logout(selenium):
    logout_button = selenium.find_element_by_id('logout_link')
    logout_button.click()

def verify_logout(selenium):
    login_button = selenium.find_element_by_id('login_link')
