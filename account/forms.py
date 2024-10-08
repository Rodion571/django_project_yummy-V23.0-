from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Your Username',
                                                                                             'class': 'form-control',
                                                                                             'id': 'username',
                                                                                             'data-rule': 'minlen:4',
                                                                                             'data-msg': 'Please enter at least 4 chars'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                            'class': 'form-control',
                                                                            'id': 'email',
                                                                            'data-rule': 'email',
                                                                            'data-msg': 'Please enter a valid email'
                                                                            }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Your Password',
                                                                                    'class': 'form-control',
                                                                                    'id': 'password1',
                                                                                    'data-rule': 'minlen:4',
                                                                                    'data-msg': 'Please enter at least 4 chars'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                                            'class': 'form-control',
                                                                                            'id': 'password2',
                                                                                            'data-rule': 'minlen:4',
                                                                                            'data-msg': 'Please enter at least 4 chars'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Your Username',
                                                                                             'class': 'form-control',
                                                                                             'id': 'username',
                                                                                             'data-rule': 'minlen:4',
                                                                                             'data-msg': 'Please enter at least 4 chars'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Your Password',
                                                                                    'class': 'form-control',
                                                                                    'id': 'password',
                                                                                    'data-rule': 'minlen:4',
                                                                                    'data-msg': 'Please enter at least 4 chars'}))
