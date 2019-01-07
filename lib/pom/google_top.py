class GoogleTop:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://www.google.com")

    @property
    def search_field(self):
        return self.driver.find_element_by_name('q')

    @property
    def google_logo(self):
        return self.driver.find_element_by_id('hplogo')
