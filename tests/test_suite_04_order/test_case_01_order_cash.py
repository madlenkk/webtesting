from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from test_suite_03_basket.test_case_01_add_item_to_basket import test as case_03_01

import pytest
@pytest.fixture
def selenium(selenium):
    # selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


def test(selenium, base_url, variables):
    # step_01_open_page
    # step_02_login
    # case_2_1(selenium, base_url, variables)
    # step_03_go_to_products
    # step_04_open_product_detail
    # step_05_add_product_to_basket
    # verify_item_added_to_basket
    case_03_01(selenium, base_url, variables)
    step_06_go_to_basket(selenium)
    step_07_proceed_to_checkout(selenium)
    step_08_fill_in_address(selenium, variables['first_name'], variables['last_name'], variables['address_line1'], variables['city'], variables['zip_code'], variables['country'])
    step_09_continue(selenium)
    step_10_continue(selenium)
    # step_11_place_order
    # step_12_check_order_id
    # step_13_check_data_displayed
    # step_14_print_page
    # step_15_close_print_dialog
    # step_16_continue_shopping


def step_06_go_to_basket(selenium):
    go_to_basket = selenium.find_element(By.XPATH, '//a[@class="btn btn-default" and contains(text(),"View basket")]')
    go_to_basket.click()

    basket_detail = selenium.find_element(By.ID, 'basket_formset')
    assert basket_detail, "Expected Result: Basket detail displayed"


def step_07_proceed_to_checkout(selenium):
    proceed_checkout = selenium.find_element(By.XPATH, '//a[@class="btn btn-lg btn-primary btn-block" and contains(text(),"Proceed to checkout")]')
    proceed_checkout.click()

    address_form = selenium.find_element(By.ID, 'new_shipping_address')
    assert address_form, "Expected Result: Form for filling the address displayed"


def step_08_fill_in_address(selenium, first_name, last_name, address_line1, city, zip_code, country):
    address_form = selenium.find_element(By.ID, 'new_shipping_address')

    field = address_form.find_element(By.ID, 'id_first_name')
    field.send_keys(first_name)

    field = address_form.find_element(By.ID, 'id_last_name')
    field.send_keys(last_name)

    field = address_form.find_element(By.ID, 'id_line1')
    field.send_keys(address_line1)

    field = address_form.find_element(By.ID, 'id_line4')
    field.send_keys(city)

    field = address_form.find_element(By.ID, 'id_postcode')
    field.send_keys(zip_code)

    field_select = address_form.find_element(By.ID, 'id_country')
    field_select.click()
    option = selenium.find_element(By.XPATH, '//select[@id="id_country"]/option[@value="%s"]' % country)
    option.click()

    # labels = address_form.find_elements(By.CLASS_NAME, 'required')
    # for label in labels:
    #     form_group = label.find_element(By.XPATH, '..')
    #     field = form_group.find_element(By.CLASS_NAME, 'form-control')
    #     assert  in field.text, "Expected Result: Mandatory fields filled in"


def step_09_continue(selenium):
    btn_continue = selenium.find_element(By.XPATH, '//button[@type="submit" and contains(text(),"Continue")]')
    btn_continue.click()


def step_10_continue(selenium):
    btn_continue = selenium.find_element(By.XPATH, '//a[@id="view_preview" and contains(text(),"Continue")]')
    btn_continue.click()


# def step_11_place_order(selenium):


# def step_12_check_order_id(selenium):


# def step_13_check_data_displayed(selenium):


# def step_14_print_page(selenium):


# def step_15_close_print_dialog(selenium):


# def step_16_continue_shopping(selenium):

