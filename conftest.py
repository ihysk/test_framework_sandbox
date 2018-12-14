import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def google():
    path = os.getenv('CHROME_DRIVER_PATH', '')
    driver = webdriver.Chrome(executable_path=path)
    driver.get("http://www.google.com")
    yield driver
    driver.quit()
