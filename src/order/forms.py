from django import forms
from .models import Contains

class ContainsForm(forms.ModelForm):
	class Meta:
		model = Contains
		fields = ['orderId', 'productId', 'quantity']

