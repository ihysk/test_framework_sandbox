import os
from selenium import webdriver


class TestGoogle:

    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH'))
        self.driver.get('http://www.google.com')

    def teardown_method(self, method):
        self.driver.close()

    def test_logo(self):
        elm = self.driver.find_element_by_id('hplogo')
        assert elm.get_attribute('alt') == 'Google'

    def test_input_field(self):
        elm = self.driver.find_element_by_name('q')
        elm.clear()
        elm.send_keys('hogehoge')
        assert elm.get_attribute('value') == 'hogehoge'
