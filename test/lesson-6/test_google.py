class TestGoogle:

    def test_logo(self, google):
        elm = google.google_logo()
        assert elm.get_attribute('alt') == 'Google'

    def test_input_field(self, google):
        elm = google.search_field()
        elm.clear()
        elm.send_keys('hogehoge')
        assert elm.get_attribute('value') == 'hogehoge'
