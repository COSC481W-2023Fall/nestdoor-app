from selenium import webdriver 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from selenium.webdriver.common.by import By
import time

class TestHeaderBar (StaticLiveServerTestCase) :

    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.close()

    def test_user_header_bar_is_displayed (self):
        self.browser.get(self.live_server_url + '/homepage')
        self.browser.maximize_window()
        assert 'Home' in self.browser.page_source
        time.sleep(5)
        self.browser.get(self.live_server_url + '/login')
        assert 'Login' in self.browser.page_source
        time.sleep(5)
        self.browser.get(self.live_server_url + '/logout')
        assert 'Logout' in self.browser.page_source
        time.sleep(5)
        self.browser.get(self.live_server_url + '/forum')
        assert 'Forum' in self.browser.page_source
        time.sleep(5)
        self.browser.get(self.live_server_url + '/about')
        assert 'About' in self.browser.page_source
        time.sleep(5)
        topnav = self.browser.find_element(By.CLASS_NAME, "topnav")
        self.assertTrue(
            topnav
        )