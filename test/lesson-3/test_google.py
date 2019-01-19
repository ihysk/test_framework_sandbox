class TestGoogle:

    def test_logo(self, google):
        elm = google.find_element_by_id('hplogo')
        assert elm.get_attribute('alt') == 'Google'

    def test_input_field(self, google):
        elm = google.find_element_by_name('q')
        elm.clear()
        elm.send_keys('hogehoge')
        assert elm.get_attribute('value') == 'hogehoge'
