from django.test import SimpleTestCase
from nestdoorapp.forms import Memberform


class TestForm(SimpleTestCase):
    
    def test_member_form_valid_data(self):
        form = Memberform(data={
            'first_name': 'Dianlu',
            'last_name': 'He' ,
            'email': 'dhe@emich.edu',
            'addr': '3000 Stone Rd',
        })

        self.assertTrue(form.is_valid)

    def test_member_form_no_data(self):
        form = Memberform(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)