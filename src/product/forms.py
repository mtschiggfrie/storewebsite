from django import forms
from .models import CreateProduct

class CreateProductForm(forms.Form):
	name = forms.CharField(widget = forms.TextInput)
	price = forms.IntegerField(widget = forms.TextInput)
	stock = forms.IntegerField(widget = forms.TextInput)
	description = forms.CharField(widget = forms.TextInput)
	active = forms.BooleanField(widget = forms.CheckboxInput, required=False)
	supplier = forms.CharField(widget = forms.TextInput)

class SearchProductForm(forms.Form):
	searchProduct = forms.CharField(widget = forms.TextInput)
	orderByPrice = forms.BooleanField(widget = forms.CheckboxInput, required=False)