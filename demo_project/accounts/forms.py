from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.shortcuts import redirect

UserModel = get_user_model()


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'gender', 'age')
        exclude = ('password',)
        labels = {'username': 'Username',
                  'email': 'Email',
                  'gender': 'Gender',
                  'age': 'Age',
                  }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "placeholder": "Username"}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "placeholder": "Password"}),
    )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {
            'username': UsernameField,
        }
