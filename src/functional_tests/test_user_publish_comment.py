from selenium import webdriver
from nestdoorapp.models import React, Member
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from nestdoorapp.models import Post
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestJoinPage (StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_user_publish_comment(self):

        Post.objects.create(title='Test Post 1',
                            content='This is a test post.')
        Post.objects.create(title='Test Post 2', content='Another test post.')

        User.objects.create_user(username='k', password='ab123abc')
        self.browser.get(self.live_server_url + '/login/')

        # Log in
        username_input = self.browser.find_element(By.ID, 'id_username')
        password_input = self.browser.find_element(By.ID, 'id_password')
        submit_button = self.browser.find_element(
            By.XPATH, '//button[@type="submit"]')

        username_input.send_keys('k')
        password_input.send_keys('ab123abc')
        submit_button.click()
        # time.sleep(10)

        # Navigate to the forum page
        # Replace with the actual URL
        self.browser.get(self.live_server_url + '/forum/')
        # time.sleep(10)

        self.browser.get(self.live_server_url + '/userpost/1')

        # time.sleep(10)

        # self.browser.find_elementby("link text", "message__button").click()
        # self.browser.find_element_by_id('message__button').click()

        # current_url = self.browser.current_url
        # expected_url = self.live_server_url + '/userpost/1'
        # self.assertEqual(current_url, expected_url)

        # Enter a value into the comment input
        comment_input = self.browser.find_element(By.ID, 'commentInput')
        comment_input.send_keys('Test Comment')

        self.browser.find_element(By.CSS_SELECTOR, ".message__button").click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'thread__details'))
        )

        comment_result = self.browser.find_element(
            By.CLASS_NAME, 'thread__details')
        self.assertEqual(comment_result.text, 'Test Comment')
