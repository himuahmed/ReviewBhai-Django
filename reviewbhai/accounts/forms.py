from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Account, Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Enter a valid email.')

    class Meta:
        model =Account
        fields=('username','email','gender','password1','password2')


class LogInForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Invalid Credentials.')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    confirm_password = forms.CharField(max_length=20,required=True, label='Enter your password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['fullname','email','confirm_password']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
