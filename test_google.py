import os
from selenium import webdriver

def test_google():
    driver = webdriver.Chrome(executable_path=os.environ['CHROME_DRIVER_PATH'])
    driver.get("http://www.google.com")

    elm = driver.find_element_by_id('hplogo')
    assert elm.get_attribute('alt') == 'Google'

    driver.quit()
