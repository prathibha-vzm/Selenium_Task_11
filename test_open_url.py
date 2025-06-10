#importing all the needed packages

import time
import pytest
from selenium.webdriver.common.by import By
from guvi_webpage.test_browser import Window


@pytest.mark.regression
def test_valid_url(driver):

    chrome_driver=driver

    chrome_driver.find_element(By.XPATH,"//a[@id='login-btn']").click() #Using XPATH to locate the login button

    time.sleep(2)

    url= chrome_driver.current_url #fetching the landing URL

    object_window=Window        #creating an object for the class and calling its method
    object_window.test_end_browser(driver)

    assert url =='https://www.guvi.in/sign-in/'  #Validating URL

@pytest.mark.sanity
def test_invalid_url(driver):
    chrome_driver = driver

    chrome_driver.find_element(By.XPATH, "//a[@id='login-btn']").click()  # Using XPATH to locate the login button

    time.sleep(2)

    url = chrome_driver.current_url  # fetching the landing URL

    object_window = Window    #creating an object for the class and calling its method
    object_window.test_end_browser(driver)

    assert url != 'https://www.guvi.in/'  # Validating URL

