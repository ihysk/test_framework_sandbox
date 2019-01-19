import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def google(request):
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH'))
    driver.get('http://www.google.com')

    yield driver

    driver.quit()
