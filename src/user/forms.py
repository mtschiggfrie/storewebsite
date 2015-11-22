from django import forms
from .models import CreateAccount

class CreateAccountForm(forms.ModelForm):
	class Meta:
		model = CreateAccount
		fields = ['id', 'name', 'address', 'password', 'email', 'is_staff']

class SignInForm(forms.ModelForm):
	class Meta:
		model = CreateAccount
		fields = ['email', 'password']