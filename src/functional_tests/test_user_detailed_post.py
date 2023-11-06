from selenium import webdriver 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from selenium.webdriver.common.by import By
import time
from django.urls import reverse

class TestUserDetailedPost (StaticLiveServerTestCase) :

    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.close()

    def test_user_detailed_post_is_displayed (self):
        self.browser.get(self.live_server_url + '/userpost')
        self.browser.maximize_window()
        time.sleep(10)
        #button = self.browser.find_element(By.CLASS_NAME, "post_content")
        #self.assertTrue(
        #    button
        #)
        detail_url = self.live_server_url + reverse("user_post")
        self.assertEquals(
            self.browser.current_url,
            detail_url
        )