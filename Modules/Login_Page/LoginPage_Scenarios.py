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
    yield
    driver.close()
# Valid credentials
def test_login_valid_credentials(setup):
    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    exp_url = "https://www.saucedemo.com/inventory.html"
    if exp_url == driver.current_url:
        print("Test Pass - Logged successfully with valid credentials")
        sleep(3)
        driver.save_screenshot('TestPass ValidCredentials.png')
    else:
        print("Test Fail - Failed to login with valid credentials")
        driver.save_screenshot('TestFail ValidCredentials.png')

# Invalid credentials
def test_login_invalid_credentials(setup):
    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user1")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce1")
    driver.find_element(By.ID, "login-button").click()
    err_msg=driver.find_element(By.XPATH, '//div[@class="error-message-container error"]').text
    if err_msg == 'Epic sadface: Username and password do not match any user in this service':
        print("Test Pass - Unable to login with invalid credentials")
        sleep(3)
        driver.save_screenshot('Test Pass-Both InvalidCredentials.png')
    else:
        print("Test Fail- Error message not display check screenshot")
        driver.save_screenshot('TestFail InvalidCredentials.png')

# valid username & invalid password
def test_login_VUIP_credentials(setup):
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce1")
    driver.find_element(By.ID, "login-button").click()
    err_msg = driver.find_element(By.XPATH, '//div[@class="error-message-container error"]').text
    if err_msg == 'Epic sadface: Username and password do not match any user in this service':
        print("Test Pass - Unable to login with invalid password")
        sleep(3)
        driver.save_screenshot('Test Pass-Invalid Password.png')
    else:
        print("Test Fail- Error message not display check screenshot")
        driver.save_screenshot('TestFail Invalid Password.png')


# Invalid username & valid password
def test_login_IUVP_credentials(setup):
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user1")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    err_msg = driver.find_element(By.XPATH, '//div[@class="error-message-container error"]').text
    if err_msg == 'Epic sadface: Username and password do not match any user in this service':
        print("Test Pass - Unable to login with invalid username")
        sleep(3)
        driver.save_screenshot('Test Pass-Invalid Username.png')
    else:
        print("Test Fail- Error message not display check screenshot")
        driver.save_screenshot('TestFail Invalid Password.png')


# Without credentials
def test_login_without_credentials(setup):
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    err_msg = driver.find_element(By.XPATH, '//div[@class="error-message-container error"]').text
    if err_msg == 'Epic sadface: Username is required':
        print("Test Pass - Unable to login without credentials")
        sleep(3)
        driver.save_screenshot('Test Pass-Without Credentials.png')
    else:
        print("Test Fail- Error message not display check screenshot")
        driver.save_screenshot('TestFail Without Credentials.png')

# Username without password
def test_login_without_password(setup):
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    err_msg = driver.find_element(By.XPATH, '//div[@class="error-message-container error"]').text
    if err_msg == 'Epic sadface: Password is required':
        print("Test Pass - Unable to login without password")
        sleep(3)
        driver.save_screenshot('Test Pass-Without Password.png')
    else:
        print("Test Fail- Error message not display check screenshot")
        driver.save_screenshot('TestFail Without Password.png')

# Password without username
def test_login_without_username(setup):
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    err_msg = driver.find_element(By.XPATH, '//div[@class="error-message-container error"]').text
    if err_msg == 'Epic sadface: Username is required':
        print("Test Pass - Unable to login without username")
        sleep(3)
        driver.save_screenshot('Test Pass-Without Username.png')
    else:
        print("Test Fail- Error message not display check screenshot")
        driver.save_screenshot('TestFail Without Username.png')
