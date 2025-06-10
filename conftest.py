import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.guvi.in/")

    return chrome_driver


