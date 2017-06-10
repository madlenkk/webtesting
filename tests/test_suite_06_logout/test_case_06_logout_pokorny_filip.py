from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from test_suite_02_login.test_case_01_valid_login import test as login

def test(selenium, base_url, variables):
    login(selenium, base_url, variables)
    logout(selenium)

def logout(selenium):
    el = selenium.find_element_by_id('logout_link')
    el.click()
