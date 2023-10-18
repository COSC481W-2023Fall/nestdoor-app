from django.test import TestCase, Client
from django.urls import reverse
from nestdoorapp.models import React
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.react_url = reverse('something')
        self.join_url = reverse('join')

        React.objects.create(name='Sample Name 1', detail='Sample Detail 1')

    
    def test_join(self):
        response = self.client.get(self.join_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'greeting.html')

    def test_react_GET(self):
        response = self.client.get(self.react_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), React.objects.count())

    def test_react_POST(self):
        

        response = self.client.post(self.react_url, data ={
            'name': 'Add Name 2',
            'detail': 'Add Detail 2'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTrue(React.objects.filter(name='Add Name 2', detail='Add Detail 2').exists())
        # print(React.objects.count())

    
        
    def test_react_POST_no_data(self):
        response = self.client.post(self.react_url)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(React.objects.count(), 1)  # 1 from setup, no new one added.