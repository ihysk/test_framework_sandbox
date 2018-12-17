def test_title_image(google):
    elm = google.find_element_by_id('hplogo')
    assert elm.get_attribute('alt') == 'Google'


def test_input_field(google):
    elm = google.find_element_by_name('q')
    elm.clear()
    elm.send_keys('hogehoge')
    assert elm.get_attribute('value') == 'hogehoge'
