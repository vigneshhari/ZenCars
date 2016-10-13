from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100)

class SignupForm(forms.Form):
	email = forms.CharField(label='email', max_length=500)
    name = forms.CharField(label='name', max_length=500)
    phone_number = forms.CharField(label='phone_number', max_length=10)
    password = forms.CharField(label='password', max_length=500)

