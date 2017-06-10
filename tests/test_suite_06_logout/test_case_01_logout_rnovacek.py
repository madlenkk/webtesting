
from test_suite_02_login.test_case_01_valid_login import (
    step_01_open_tested_page,
    step_02_click_on_login,
    step_03_fill_username,
    step_04_fill_password,
    step_05_click_submit,
)


def test(selenium, base_url, variables):
    step_01_open_page(selenium, base_url)
    step_02_login_valid(selenium, variables['username'], variables['password'])
    step_03_logout(selenium)


def step_01_open_page(selenium, base_url):
    step_01_open_tested_page(selenium, base_url)


def step_02_login_valid(selenium, username, password):
    step_02_click_on_login(selenium)
    step_03_fill_username(selenium, username)
    step_04_fill_password(selenium, password)
    step_05_click_submit(selenium)


def step_03_logout(selenium):
    selenium.find_element_by_id('logout_link').click()
    assert selenium.find_element_by_id('login_link')
