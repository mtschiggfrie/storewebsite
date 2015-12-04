from django import forms
from .models import Contains

class ContainsForm(forms.ModelForm):
	class Meta:
		model = Contains
		fields = ['productId', 'quantity']

class PayForm(forms.Form):
	total = forms.IntegerField(widget = forms.TextInput(attrs={'readonly':'readonly'}), required=False)

class DeleteCartForm(forms.Form):
	orderId = forms.IntegerField(widget = forms.TextInput, required=False)