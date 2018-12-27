import os
import pytest
from selenium import webdriver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope='function', autouse=True)
def google(request):
    if 'CHROME_DRIVER_PATH' in os.environ:
        driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH'))
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.google.com")
    yield driver
    if request.node.rep_call.failed:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, 'screenshot-{}.png'.format(request.node.name))
        try:
            driver.save_screenshot(file_path)
        except IOError as e:
            print('I/O error({0}): {1}'.format(e.errno, e.strerror))
    driver.quit()
