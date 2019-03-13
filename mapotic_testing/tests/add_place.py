from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

from selenium.webdriver import ActionChains


def add_place(selenium, variables):
    """Add new place
    """

    btn_add_place = selenium.find_element(By.CLASS_NAME, 'navbar--add-place')
    btn_add_place.click()

    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'new')))

    # # Add place by clicking in map window
    # map = selenium.find_element(By.CLASS_NAME, 'map-component')
    # action = ActionChains(selenium)
    # action.move_to_element_with_offset(map, 1000, 500)
    # action.click().perform()

    # Add place by inserting coordinates to inputbox
    inputs = selenium.find_elements(By.CLASS_NAME, 'mat-input-element')
    input_place = inputs[0]
    input_place.send_keys(variables['place_coordinates'])
    WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'mat-autocomplete-visible')))
    options = selenium.find_elements(By.CLASS_NAME, 'mat-option')
    options[0].click()

    inputs = selenium.find_elements(By.CLASS_NAME, 'mat-input-element')
    input_name = inputs[1]
    input_name.send_keys(variables['place_name'])

    place_category = selenium.find_element(By.CLASS_NAME, 'mat-select')
    place_category.click()
    place_category_value = selenium.find_element(By.XPATH, '//span[contains(text(), "%s")]' % variables['place_category'])
    # place_category_value = selenium.find_element(By.CLASS_NAME, 'mat-option-text')
    place_category_value.click()

    btn_submit = selenium.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    btn_submit.click()

    WebDriverWait(selenium, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'new')))

    place_header = selenium.find_element(By.CLASS_NAME, 'header-panel')

    place_title = place_header.find_element(By.CLASS_NAME, 'title')
    assert place_title.text == variables['place_name']

    place_category = place_header.find_element(By.CLASS_NAME, 'subtitle')
    assert place_category.text == variables['place_category']
