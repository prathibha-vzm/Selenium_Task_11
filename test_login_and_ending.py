#importing all the packages needed

import time
import pytest
from selenium.webdriver.common.by import By
from guvi_webpage.test_browser import Window


@pytest.mark.smoke
def test_valid_login(driver):
    chrome_driver = driver

    chrome_driver.find_element(By.XPATH,
                               "//a[@id='login-btn']").click() #Using XPATH to locate the login button

    email=chrome_driver.find_element(By.XPATH,
                               "//input[@id='email']")     #Using ID to input Username

    if email.is_displayed() and email.is_enabled():
        email.send_keys("vigneswaranprathibha@gmail.com")
    time.sleep(5)

    password=chrome_driver.find_element(By.CSS_SELECTOR,
                               "input[id='password']")  #Using ID to input password

    if password.is_displayed() and password.is_enabled():
        password.send_keys("VZidane$23")


    login=chrome_driver.find_element(By.XPATH, #Using XPATH to locate the login button
                               "//a[@class='btn login-btn']") #Is enabled is used to check the successful login

    if login.is_enabled():
        login.click()

    time.sleep(5)

    url_this=chrome_driver.current_url

    object_window = Window             #creating an object for the class and calling its method
    object_window.test_end_browser(driver)

    assert url_this == 'https://www.guvi.in/courses/?current_tab=myCourses'

@pytest.mark.sanity
def test_invalid_login(driver):
    chrome_driver = driver

    # Using XPATH to locate the login button
    chrome_driver.find_element(By.XPATH,
                               "//a[@id='login-btn']").click()

    # Using ID to input Username
    email= chrome_driver.find_element(By.ID,
                               'email')
    if email.is_displayed() and email.is_enabled(): # checking email input box's status
        email.send_keys("prathibha@gmail.com")

    # Using ID to input invalid password
    password=chrome_driver.find_element(By.ID,
                               'password')
    if password.is_displayed() and password.is_enabled(): # checking password input box's status
        password.send_keys("VZidane23")

    # Using XPATH to locate the login button
    # Is enabled is used to check the successful login
    login=chrome_driver.find_element(By.XPATH,
                               "//a[@class='btn login-btn']")

    if login.is_enabled(): # checking the login buttons status
        login.click()
    time.sleep(5)

    url = chrome_driver.current_url # fetching the current URL

    object_window = Window            #creating an object for the class and calling its method
    object_window.test_end_browser(driver)

    assert url != 'https://www.guvi.in/courses/?current_tab=myCourses'
    # checking the url from the landing page is not equal o the expected one