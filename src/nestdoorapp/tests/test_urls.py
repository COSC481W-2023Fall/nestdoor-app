from django.test import SimpleTestCase
from django.urls import reverse, resolve
from nestdoorapp.views import join, name_list, ReactView


class TestUrls(SimpleTestCase):
    
    def test_join_url_is_resolved(self):
        url = reverse('join')
        self.assertEqual(resolve(url).func, join)

    
    def test_react_url_is_resolved(self):
        url = reverse('something')
        self.assertEqual(resolve(url).func.view_class, ReactView)
    

    def test_name_list_url_is_resolved(self):
        url = reverse('name_list')
        self.assertEqual(resolve(url).func, name_list)