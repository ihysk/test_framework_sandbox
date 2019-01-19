from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoogle:

    def test_logo(self, google):
        elm = WebDriverWait(google, 10).until(EC.presence_of_element_located((By.ID, 'hplogo')))
        assert elm.get_attribute('alt') == 'Google'

    def test_input_field(self, google):
        elm = WebDriverWait(google, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        elm.clear()
        elm.send_keys('hogehoge')
        assert elm.get_attribute('value') == 'hogehoge'
