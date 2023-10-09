from django.test import TestCase
from nestdoorapp.models import React


class ReactModelTestCase(TestCase):

    def setUp(self):
        # Create some sample React objects for testing
        React.objects.create(name='Sample Name 1', detail='Sample Detail 1')
        React.objects.create(name='Sample Name 2', detail='Sample Detail 2')

    def test_react_model_str(self):
        react_obj = React.objects.get(name='Sample Name 1', detail='Sample Detail 1')
        
        # Check the __str__ method of the model
        self.assertEqual(str(react_obj), 'Sample Name 1 Sample Detail 1')

    def test_react_model_fields(self):
        react_obj = React.objects.get(name='Sample Name 2', detail='Sample Detail 2')

        # Check individual fields of the model
        self.assertEqual(react_obj.name, 'Sample Name 2')
        self.assertEqual(react_obj.detail, 'Sample Detail 2')

    def test_react_model_creation(self):
        # Check if the objects were created successfully
        self.assertEqual(React.objects.count(), 2)