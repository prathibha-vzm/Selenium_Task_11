# Selenium_Task_11
Selenium Task

Commands used to run the HTML report***

pytest --ignore=Lib -m smoke --html=loginreport.html
pytest --ignore=Lib -m sanity --html=invalidloginreport.html
pytest --ignore=Lib -m regression --html=validate_url_report.html
