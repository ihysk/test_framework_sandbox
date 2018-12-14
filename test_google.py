def test_google(google):
    elm = google.find_element_by_id('hplogo')
    assert elm.get_attribute('alt') == 'Google'
