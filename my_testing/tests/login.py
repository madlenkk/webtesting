from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

from selenium.webdriver import ActionChains

import pytest
import time

from .user_dropdown import show_dropdown, hide_dropdown


def signup(selenium):
    """Open signup form
    """

    btn_login = selenium.find_element(By.CLASS_NAME, 'login-btn')
    btn_login.click()

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'signup-form')))


def login_valid(selenium, variables):
    """Test regular login with valid credentials
    """

    signup(selenium)

    signup_form = selenium.find_element(By.CLASS_NAME, 'signup-form')

    input_email = signup_form.find_element(By.CSS_SELECTOR, 'input[name=email]')
    input_email.send_keys(variables['username'])

    input_pswd = signup_form.find_element(By.CSS_SELECTOR, 'input[name=password]')
    input_pswd.send_keys(variables['password'])

    btn_login_submit = signup_form.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    btn_login_submit.click()

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'my-mapotic-wrap')))

    assert "/my/stream" in selenium.current_url

    show_dropdown(selenium)

    assert selenium.find_element(By.CLASS_NAME, 'subheading').text == variables['username']

    hide_dropdown(selenium)


def logout(selenium):
    """Test logout from app
    """

    show_dropdown(selenium)

    btn_logout = selenium.find_element(By.CSS_SELECTOR, 'a[gaaction=Logout]')
    btn_logout.click()

    WebDriverWait(selenium, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'dropdown-content')))

    with pytest.raises(NoSuchElementException, message='USER DROPDOWN STILL PRESENT'):
        selenium.find_element(By.CLASS_NAME, 'profile-thumb')

    time.sleep(1)

    assert "/dashboard" in selenium.current_url
    assert "/my/stream" not in selenium.current_url


def login_invalid(selenium, variables):
    """Test regular login with invalid credentials
    """

    signup(selenium)

    signup_form = selenium.find_element(By.CLASS_NAME, 'signup-form')

    btn_login_submit = signup_form.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    btn_login_submit.click()
    error_messages = signup_form.find_elements(By.CLASS_NAME, 'error-message')
    assert len(error_messages) == 2

    input_email = signup_form.find_element(By.CSS_SELECTOR, 'input[name=email]')
    input_email.send_keys(variables['username_invalid'])

    btn_login_submit.click()
    error_messages = signup_form.find_elements(By.CLASS_NAME, 'error-message')
    assert len(error_messages) == 1

    input_pswd = signup_form.find_element(By.CSS_SELECTOR, 'input[name=password]')
    input_pswd.send_keys(variables['password_invalid'])

    show_pswd = signup_form.find_element(By.CLASS_NAME, 'show-password-icon')
    show_pswd.click()
    input_pswd_type = input_pswd.get_attribute("type")
    assert input_pswd_type == 'text'

    hide_pswd = signup_form.find_element(By.CLASS_NAME, 'show-password-icon')
    hide_pswd.click()
    input_pswd_type = input_pswd.get_attribute("type")
    assert input_pswd_type == 'password'

    btn_login_submit.click()
    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'error-message')))
    error_messages = signup_form.find_elements(By.CLASS_NAME, 'error-message')
    assert len(error_messages) == 1

    input_email.clear()
    input_email.send_keys(variables['username'])

    btn_login_submit.click()
    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'error-message')))
    error_messages = signup_form.find_elements(By.CLASS_NAME, 'error-message')
    assert len(error_messages) == 1


def login_cancel(selenium):
    """Cancel login by clicking out of the signup form
    """

    backdrop = selenium.find_element(By.CLASS_NAME, 'modal-backdrop')

    action = ActionChains(selenium)
    action.move_to_element_with_offset(backdrop, 100, 100)
    action.click().perform()

    WebDriverWait(selenium, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'signup-form')))
