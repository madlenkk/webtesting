from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_suite_02_login.test_case_01_valid_login import test as login_test


def test(selenium, base_url, variables):
    login_test(selenium, base_url, variables)

    click_logout(selenium)

    verify_logout(selenium)


def click_logout(selenium):
    el = selenium.find_element_by_link_text('Logout')
    el.click()


def verify_logout(selenium):
    el = selenium.find_element_by_id('login_link')
    assert 'Login or register' in el.text