from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class AuthForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),)

    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

class Registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        labels = {
            'username': 'Username',
        }
        help_texts = {
            'username': '',
        }

    def __init__(self, *args, **kwargs):
        super(Registerform, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Repeat Password'
        self.fields['password1'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password2'].help_text = ''