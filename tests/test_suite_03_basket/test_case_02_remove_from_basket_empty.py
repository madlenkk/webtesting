from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from test_suite_03_basket.test_case_01_add_item_to_basket import test as case_03_01
from test_suite_04_order.test_case_01_order_cash import step_06_go_to_basket as step_04_01_06

import pytest
@pytest.fixture
def selenium(selenium):
    # selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


def test(selenium, base_url, variables):
    case_03_01(selenium, base_url, variables)
    # step_01_open_page
    # step_02_login
    step_02_remove_item_from_basket(selenium)
    step_03_check_basket_is_empty(selenium)

def step_02_remove_item_from_basket(selenium):
    step_04_01_06(selenium)

    remove_button = selenium.find_element(By.XPATH, '//a[contains(text(),"Remove")]')
    remove_button.click()

def step_03_check_basket_is_empty(selenium):
    # //*[@id="messages"]/div[2]/p
    # pytest.set_trace()
    # el = selenium.find_element_by_id('messages')
    # import time
    # time.sleep(1)
    # assert 'Your basket is now empty' in el.text

    WebDriverWait(selenium, 2).until(
        EC.text_to_be_present_in_element(
            # (By.ID, 'messages'),
            (By.XPATH, '//p[contains(text(),"Your basket is now empty")]'),
            'Your basket is now empty'
         )
    )

    # empty_alert = selenium.find_element(By.XPATH,'//p[contains(text(),"Your basket is now empty")]')
