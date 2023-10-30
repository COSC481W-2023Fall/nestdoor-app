from django import forms
from .models import Member, Post
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostCreationForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':50}))

    class Meta:
        model = Post
        fields = ('content', 'posted_by')

    def clean(self):
        content = self.cleaned_data['content']
        posted_by = self.cleaned_data['posted_by']
        if not save(content=content):
            raise forms.ValidationError("No content.")


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid login.")


class Memberform(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'addr']
        
