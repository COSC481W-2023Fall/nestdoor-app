from selenium import webdriver 
from nestdoorapp.models import React, Member 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from django.urls import reverse
import time

class TestProjectListPage (StaticLiveServerTestCase) :

    def setUp(self):
        # self.browser = webdriver.Chrome('functional_tests/chromedriver')
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.close()

    def test_nothing(self):
        self.browser.get(self.live_server_url)
        time.sleep(60)

