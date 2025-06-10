#importing needed packages

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def driver():

    chrome_options=Options()

    #headless run
    #chrome_options.add_argument("--headless")

    # to avoid ElementNotInteractableException due to graphical content
    chrome_options.add_argument("--disable-gpu")

    # To set window size
    chrome_options.add_argument("--window-size=720,880")

    #To create chrome driver
    chrome_driver = webdriver.Chrome(chrome_options)

    #to open the URL(Web page)
    chrome_driver.get("https://www.guvi.in/")


    return chrome_driver


