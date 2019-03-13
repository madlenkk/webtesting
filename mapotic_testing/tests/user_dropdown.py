from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

import time


def show_dropdown(selenium):
    """
    """

    time.sleep(1)

    # WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'profile-thumb')))

    dropdown = selenium.find_element(By.CLASS_NAME, 'profile-thumb')
    dropdown.click()

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'dropdown-content')))


def hide_dropdown(selenium):
    """
    """

    dropdown = selenium.find_element(By.CLASS_NAME, 'dropdown')
    dropdown.click()

    WebDriverWait(selenium, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'dropdown-content')))
