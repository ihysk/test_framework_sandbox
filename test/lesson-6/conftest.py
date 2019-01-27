import os
import pytest
from selenium import webdriver

from page.google_top import GoogleTop


@pytest.fixture(scope='function', autouse=True)
def google(request):
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH'))
    google = GoogleTop(driver)
    google.open()

    yield google

    driver.quit()
