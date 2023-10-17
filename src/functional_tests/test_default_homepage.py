from selenium import webdriver 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from selenium.webdriver.common.by import By
import time

class TestHomePageView (StaticLiveServerTestCase) :

    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.close()

    def test_user_homepage_view_is_displayed (self):
        self.browser.get(self.live_server_url + '/homepage')
        self.browser.maximize_window()
        time.sleep(10)
        button = self.browser.find_element(By.LINK_TEXT, "Home")
        self.assertTrue(
            button
        )