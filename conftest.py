import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def google():
    if 'CHROME_DRIVER_PATH' in os.environ:
        driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH'))
    else:
        driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    yield driver
    driver.quit()
