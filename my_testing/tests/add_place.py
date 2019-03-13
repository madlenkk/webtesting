from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

import time


def add_place(selenium, variables):
    """Test add place
    """

    add_place_btn = selenium.find_element(By.CLASS_NAME, 'navbar--add-place')
    add_place_btn.click()

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'new')))

    inputs = selenium.find_elements(By.CLASS_NAME, 'mat-input-element')
    inputs[0].send_keys(variables['place_coordinates'])

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located
    ((By.CLASS_NAME, 'mat-autocomplete-visible')))

    option = selenium.find_element(By.CLASS_NAME, 'mat-option')
    option.click()

    inputs = selenium.find_elements(By.CLASS_NAME, 'mat-input-element')
    inputs[1].send_keys(variables['place_name'])

    place_category = selenium.find_element(By.CLASS_NAME, 'mat-select')
    place_category.click()

    place_options = selenium.find_elements(By.CLASS_NAME, 'mat-option-text')
    place_options[0].click()

    btn_submit = selenium.find_element
    (By.CSS_SELECTOR, 'button[type=submit]')
    btn_submit.click()

    WebDriverWait(selenium, 5).until(EC.invisibility_of_element_located
    ((By.CLASS_NAME, 'new')))

    place_header = selenium.find_element(By.CLASS_NAME, 'header-panel')

    place_title = place_header.find_element(By.CLASS_NAME, 'title')
    assert place_title.text == variables['place_name']

    place_category = place_header.find_element(By.CLASS_NAME, 'subtitle')
    assert place_category.text == variables['place_category']
