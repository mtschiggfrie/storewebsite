from django import forms
from .models import CreateAccount

class CreateAccountForm(forms.ModelForm):
	class Meta:
		model = CreateAccount
		fields = ['id', 'name', 'address', 'password', 'email']

class SignInForm(forms.ModelForm):
	class Meta:
		model = CreateAccount
		fields = ['email', 'password']

class UpdateAccountForm(forms.Form):
	name = forms.CharField(widget = forms.TextInput)
	address = forms.CharField(widget = forms.TextInput)
	password = forms.CharField(widget = forms.TextInput)
	email = forms.EmailField(widget = forms.EmailInput)
