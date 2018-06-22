from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver import FirefoxOptions


class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = FirefoxOptions()
        opts.add_argument("--headless")  # Necessary for servers without a display (travis-ci)
        cls.selenium = WebDriver(firefox_options=opts)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()  # close Firefox when tests are done
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('myapp:myview')))
        assert self.selenium.title == "", "Should be an empty page, because no template"
