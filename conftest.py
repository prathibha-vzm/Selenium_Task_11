#importing the needed packages
import pytest
from selenium import webdriver


@pytest.fixture 
def driver():
    
    chrome_driver = webdriver.Chrome() #To open the browser
    
    chrome_driver.get("https://www.guvi.in/")  #to open the url(webpage)

    return chrome_driver


