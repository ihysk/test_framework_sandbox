from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleTopLoc:
    top_image = (By.ID, 'hplogo')
    input_form = (By.NAME, 'q')


class GoogleTop:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://www.google.com")

    def search_field(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(GoogleTopLoc.input_form))

    def google_logo(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(GoogleTopLoc.top_image))
