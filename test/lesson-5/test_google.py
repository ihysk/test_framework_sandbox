from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleLocator:
    top_image = (By.ID, 'hplogo')
    input_form = (By.NAME, 'q')


class TestGoogle:

    def test_logo(self, google):
        elm = WebDriverWait(google, 10).until(EC.presence_of_element_located(GoogleLocator.top_image))
        assert elm.get_attribute('alt') == 'Google'

    def test_input_field(self, google):
        elm = WebDriverWait(google, 10).until(EC.presence_of_element_located(GoogleLocator.input_form))
        elm.clear()
        elm.send_keys('hogehoge')
        assert elm.get_attribute('value') == 'hogehoge'
