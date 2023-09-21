from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.")
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-4 px-6 roundex-xl', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-4 px-6 roundex-xl', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-4 px-6 roundex-xl', 'placeholder': 'Last Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'w-full py-4 px-6 roundex-xl', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 roundex-xl', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 roundex-xl', 'placeholder': 'Confirm Password'}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-4 px-6 roundex-xl', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 roundex-xl', 'placeholder': 'Password'}))