from django import forms
from .models import Member


class Memberform(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'addr']