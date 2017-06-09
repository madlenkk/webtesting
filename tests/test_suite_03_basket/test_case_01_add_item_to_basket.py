from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from test_suite_02_login.test_case_01_valid_login import test as case_02_01

import pytest
@pytest.fixture
def selenium(selenium):
    # selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


def test(selenium, base_url, variables):
    # step_01_open_page
    # step_02_login
    case_02_01(selenium, base_url, variables)

    step_03_go_to_products(selenium, variables["category"])
    step_04_open_product_detail(selenium, variables["product_name"])
    step_05_add_product_to_basket(selenium)

    verify_item_added_to_basket(selenium, variables["product_name"])


def step_03_go_to_products(selenium, category):
    menu_bar_item = selenium.find_element(By.XPATH,
        '//div[@class="side_categories"]//a[contains(text(),"' + category + '")]')
    menu_bar_item.click()


def step_04_open_product_detail(selenium, product_name):
    product = selenium.find_element(By.XPATH, '//a[contains(@title,"' + product_name + '")]')
    product.click()


def step_05_add_product_to_basket(selenium):
    add_to_basket = selenium.find_element(By.XPATH, '//button[@type="submit" and contains(text(),"Add to basket")]')
    add_to_basket.click()

def verify_item_added_to_basket(selenium, product_name):
    message = selenium.find_element(By.XPATH, '//div[@class="alertinner "]/strong[contains(text(),"'+ product_name + '")]')
