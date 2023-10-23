from selenium import webdriver 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from selenium.webdriver.common.by import By
import time
from django.urls import reverse

class TestHeaderBar (StaticLiveServerTestCase) :

    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.close()

    def test_user_header_bar_is_displayed (self):
        self.browser.get(self.live_server_url + '/homepage')
        self.browser.maximize_window()
        detail_url = self.live_server_url + reverse("home")
        self.assertEquals(
            self.browser.current_url,
            detail_url
        )
        time.sleep(5)
        self.browser.get(self.live_server_url + '/login')
        detail_url = self.live_server_url + reverse("login")
        self.assertEquals(
            self.browser.current_url,
            detail_url
        )
        time.sleep(5)
        self.browser.get(self.live_server_url + '/logout')
        detail_url = self.live_server_url + reverse("logout")
        self.assertEquals(
            self.browser.current_url,
            detail_url
        )
        time.sleep(5)
        self.browser.get(self.live_server_url + '/forum')
        detail_url = self.live_server_url + reverse("forum")
        self.assertEquals(
            self.browser.current_url,
            detail_url
        )
        time.sleep(5)
        self.browser.get(self.live_server_url + '/about')
        detail_url = self.live_server_url + reverse("about")
        self.assertEquals(
            self.browser.current_url,
            detail_url
        )
        time.sleep(5)
        topnav = self.browser.find_element(By.CLASS_NAME, "topnav")
        self.assertTrue(
            topnav
        )
        