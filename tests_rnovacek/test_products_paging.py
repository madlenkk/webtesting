

def find_page_products(selenium):
    return selenium.find_elements_by_css_selector('.page_inner .product_pod')


def get_product_name(product):
    return product.find_element_by_css_selector('h3').text


def test_products_paging(selenium, base_url):
    selenium.get(base_url)
    products_first_page = find_page_products(selenium)
    assert len(products_first_page) == 20
    first_page_names = {get_product_name(product) for product in products_first_page}

    selenium.find_element_by_css_selector('.pager .next a').click()
    products_second_page = find_page_products(selenium)
    assert len(products_second_page) == 20

    for product in products_second_page:
        product_name = get_product_name(product)
        assert product_name not in first_page_names
