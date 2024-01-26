from time import sleep

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture
def setup():
    global driver
    ch_options = Options()
    ch_options.add_experimental_option('detach', True)
    ch_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=ch_options)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    exp_url = "https://www.saucedemo.com/inventory.html"
    if exp_url == driver.current_url:
        print("Test Pass - Logged successfully with valid credentials")
        driver.save_screenshot('TestPass ValidCredentials.png')
    else:
        print("Test Fail - Failed to login with valid credentials")
        driver.save_screenshot('TestFail ValidCredentials.png')

def test_addremove_product(setup):
    print('Product Add functionality test')
    product_add= driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    product_add.click()
    cart=driver.find_element(By.XPATH, "//span[contains(text(),'1')]")
    if cart.text== '1':
        print("Test Pass - Products added successfully")
        driver.save_screenshot('Test Pass - Products added successfully')
    else:
        print('Test Fail-Product not added')
        driver.save_screenshot('Test Fail - Products not added')
    print('Product remove functionality test')
    sleep(2)
    product_remove = driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
    product_remove.click()
    if driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").is_displayed():
        print('Test Pass - Products removed successfully')
        driver.save_screenshot('Test Pass - Products removed successfully')
    else:
        print('Test Fail-Product removed added')
        driver.save_screenshot('Test Fail-Product not removed')


def test_checkout_positive(setup):
    product_add = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    product_add.click()
    cart = driver.find_element(By.XPATH, "//span[contains(text(),'1')]")
    if cart.text == '1':
        print("Test Pass - Products added successfully")
        cart.click()
    else:
        print("Test Fail-Product not added")
    driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys('Test_First_Name')
    driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys('Test_Last_Name')
    driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("524001")
    driver.find_element(By.XPATH,"//input[@id='continue']").click()
    checkout = driver.find_element(By.XPATH, "//button[@id='finish']")
    if checkout.is_displayed():
        checkout.click()
        if driver.find_element(By.XPATH, "//h2[contains(text(),'Thank you for your order!')]").text == "Thank you for your order!":
            print("Test Pass-Order Placed Sucessfully")
        else:
            print("Test Fail-Order Not Placed Sucessfully")
    else:

        print("Test Fail-Checkout Page Not Display")


