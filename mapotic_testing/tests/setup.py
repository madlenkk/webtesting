from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException


def load_app(selenium, base_url):
    """Open application url
    """

    selenium.get(base_url)

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'header-bar')))

    navbar = selenium.find_element(By.CLASS_NAME, 'centered-content-md')
    assert navbar

    logo = navbar.find_element(By.CLASS_NAME, 'navbar-logo')
    assert logo


def cookie_close(selenium):
    """Close cookie notice
    """

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.ID, 'cookie-bar')))

    cookie_bar = selenium.find_element(By.ID, 'cookie-bar')
    btn_cookie_close = cookie_bar.find_element(By.CLASS_NAME, 'btn')
    btn_cookie_close.click()

    WebDriverWait(selenium, 5).until(EC.invisibility_of_element_located((By.ID, 'cookie-bar')))
