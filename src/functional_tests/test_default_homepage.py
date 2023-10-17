from selenium import webdriver 
from nestdoorapp.models import React, Member 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from django.urls import reverse
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