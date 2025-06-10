#creating a class and method to close the browser and end automation

class Window:

    @staticmethod
    def test_end_browser(driver):

        chrome_driver = driver

        chrome_driver.close()  # to close the browser

        chrome_driver.quit()  # to stop the automation process