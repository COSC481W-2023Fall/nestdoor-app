from selenium import webdriver 
from nestdoorapp.models import React, Member 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from django.urls import reverse
import time

class TestHeaderBar (StaticLiveServerTestCase) :

    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.close()

    def test_user_header_bar_is_displayed (self):
        self.browser.get(self.live_server_url + '/homepage')
        self.browser.maximize_window()
        time.sleep(5)
        self.browser.get(self.live_server_url + '/login')
        time.sleep(5)
        self.browser.get(self.live_server_url + '/logout')
        time.sleep(5)
        self.browser.get(self.live_server_url + '/forum')
        time.sleep(5)
        self.browser.get(self.live_server_url + '/about')
        time.sleep(5)