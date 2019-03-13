from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException


def find_map(selenium, variables):
    """Find testing map
    """

    discover_btn = selenium.find_element(By.CLASS_NAME, 'mapotic-normal-button')
    discover_btn.click()

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'browser-container')))

    input_search = selenium.find_element(By.CLASS_NAME, 'search-input')
    input_search.send_keys(variables['map_name'])

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'results-item')))

    result = selenium.find_elements(By.CLASS_NAME, 'results-item')
    item_title = result[0].find_element(By.CLASS_NAME, 'results-item-content').get_attribute('title')
    assert variables['map_name'] == item_title
    result[0].click()

    sidebar = WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'map-sidebar-content')))
    assert sidebar

    map = selenium.find_element(By.CLASS_NAME, 'map-component')
    assert map

    map_title = selenium.find_element(By.CLASS_NAME, 'title')
    assert variables['map_name'] in map_title.text

    assert variables['map_name'].lower() in selenium.current_url
