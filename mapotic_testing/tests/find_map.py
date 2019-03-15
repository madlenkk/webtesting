from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException


def find_map(selenium, variables):
    """Find testing map
    """

    input_search = selenium.find_element(By.CLASS_NAME, 'input-normal')
    input_search.send_keys(variables['map_name'])

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'mat-nav-list')))

    ## Simple method - works correctly with only 1 result in the list
    # result = selenium.find_element(By.CLASS_NAME, 'custom-list-item')
    # result.click()

    ## Complex and correct method
    results = selenium.find_elements(By.CLASS_NAME, 'custom-list-item')
    item_title = results[0].find_element(By.CLASS_NAME, 'custom-list-item-title').text
    assert variables['map_name'] == item_title
    results[0].click()

    sidebar = WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'map-sidebar-content')))
    assert sidebar

    map = selenium.find_element(By.CLASS_NAME, 'map-component')
    assert map

    map_title = selenium.find_element(By.CLASS_NAME, 'title')
    assert variables['map_name'] in map_title.text

    assert variables['map_name'].lower() in selenium.current_url
