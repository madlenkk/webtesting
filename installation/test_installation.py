from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chromedriver binary must be in PATH
browser = webdriver.Chrome('chromedriver')
browser.get('https://github.com/madlenkk/webtesting/blob/master/installation/test_page.md')

try:
    img = browser.find_element_by_xpath('//*[@id="readme"]/article/p[1]/a/img')
    img.click()

    re = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, 'page-container'))
    )

    button = browser.find_element_by_class_name('ytp-fullscreen-button')
    button.click()

    re = WebDriverWait(browser, 50).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'ytp-upnext-top'))
    )

    print("Všechno se povedlo - třikrát zatleskej, zvolej 'juchů' a vyvěš zelený papírek!")

except:
    print("Něco je špatně - krátce  pískni a vyvěš červený papírek.")

finally:
    browser.quit()
