from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test(selenium, base_url, variables):
    step_01_open_tested_page(selenium, base_url)
    step_02_click_on_login(selenium)
    step_03_fill_username(selenium, variables['invalid_username'])
    step_04_fill_password(selenium, variables['invalid_password'])
    step_05_click_submit(selenium)


def step_01_open_tested_page(selenium, base_url):
    selenium.get(base_url)

def step_02_click_on_login(selenium):
    el = selenium.find_element_by_link_text('Login or register')
    el.click()

def step_03_fill_username(selenium, username):
    el = selenium.find_element_by_id('id_login-username')
    el.send_keys(username)

def step_04_fill_password(selenium, password):
    el = selenium.find_element_by_id('id_login-password')
    el.send_keys(password)

def step_05_click_submit(selenium):
    el = selenium.find_element_by_name('login_submit')
    el.click()

    # kdyz potrebujeme otestovat, ze na strance je nejaky konkretni element
    # el = selenium.find_element_by_xpath('//*[@id="login_form"]/div[1]/strong')
    # vynechame nefunkcni identifikatory pro pripad, ze se zmeni HTML sablona
    el = selenium.find_element_by_id('login_form')

    # kdyz potrebujeme zjistit, ze element obsahuje konkretni text
    assert 'Oops!' in el.text



