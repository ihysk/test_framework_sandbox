import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def google():
    driver = webdriver.Chrome(executable_path=os.environ['CHROME_DRIVER_PATH'])
    driver.get("http://www.google.com")
    yield driver
    driver.quit()


def test_google(google):
    elm = google.find_element_by_id('hplogo')
    assert elm.get_attribute('alt') == 'Google'
