from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import ContactModel

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="username",max_length=100,required=True)
    email = forms.EmailField(label="email",max_length=100,required=True)
    password = forms.CharField(label="password",max_length=100,required=True)
    confirm_password = forms.CharField(label="confirm_password",max_length=100,required=True)

    class Meta:
        model = User 
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Password mismatch')

class ContactForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(max_length=100,required=True)
    message = forms.CharField(required=True)

    class Meta:
        model = ContactModel
        fields = ['username','email','message']

class LoginForm(forms.Form):
    username = forms.CharField(label="username",max_length=100,required=True)
    password = forms.CharField(label="password",max_length=100,required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if user is None:
                raise forms.ValidationError("Invalid Username/Password")

