import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def google():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    if 'CHROME_DRIVER_PATH' in os.environ:
        driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH'), options=chrome_options)
    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.google.com")
    yield driver
    driver.quit()
