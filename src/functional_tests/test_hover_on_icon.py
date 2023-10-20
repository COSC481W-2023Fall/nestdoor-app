from selenium import webdriver 
from nestdoorapp.models import React, Member 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from django.urls import reverse
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestJoinPage (StaticLiveServerTestCase) :

    def setUp(self):
        # self.browser = webdriver.Chrome('functional_tests/chromedriver')
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.close()

    # def test_nothing(self):
    #     self.browser.get(self.live_server_url)
    #     time.sleep(60)

    # def test_user_is_redirected_to_view2(self):
    #     self.browser.get(self.live_server_url + '/views/view1')
    #     # print(self.live_server_url)
    #     detail_url = self.live_server_url + reverse('name_list')
    #     #print(detail_url)
    #     self.browser.find_element("link text", "Go back to User List").click()
    #     self.assertEquals(
    #         self.browser.current_url,
    #         detail_url
    #     )


    def test_hover_over_element(self):
        self.browser.get(self.live_server_url + '/homepage')

        element = self.browser.find_element(By.CSS_SELECTOR, 'a[href="/homepage"]')
        # find_element_by_css_selector('a[href="/homepage"]').hover()

        # Create an ActionChains object
        actions = ActionChains(self.browser)

        # Perform the hover action
        actions.move_to_element(element).perform()



