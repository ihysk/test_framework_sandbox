import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def google():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    if 'CHROME_DRIVER_PATH' in os.environ:
        driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH'), chrome_options=chrome_options)
    else:
        driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://www.google.com")
    yield driver
    driver.quit()
