from django import forms

class DeleteProductForm(forms.Form):
	deleteProduct = forms.IntegerField(widget = forms.TextInput)

class ProductLookUpForm(forms.Form):
	ProductId = forms.IntegerField(widget = forms.TextInput)

class UpdateProductForm(forms.Form):
	id = forms.IntegerField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
	name = forms.CharField(widget = forms.TextInput)
	price = forms.IntegerField(widget = forms.TextInput)
	stock = forms.IntegerField(widget = forms.TextInput)
	description = forms.CharField(widget = forms.TextInput)
	active = forms.BooleanField(widget = forms.CheckboxInput, required=False)

class DeleteUserForm(forms.Form):
	deleteUser = forms.IntegerField(widget = forms.TextInput)

class UserLookUpForm(forms.Form):
	UserId = forms.IntegerField(widget = forms.TextInput)

class UpdateUserForm(forms.Form):
	id = forms.IntegerField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
	name = forms.CharField(widget = forms.TextInput)
	address = forms.CharField(widget = forms.TextInput)
	password = forms.CharField(widget = forms.TextInput)
	email = forms.EmailField(widget = forms.EmailInput)
	is_staff = forms.BooleanField(widget = forms.CheckboxInput, required=False)

class DeleteOrderForm(forms.Form):
	deleteOrder = forms.IntegerField(widget = forms.TextInput)

class ChangePaidForm(forms.Form):
	orderId = forms.IntegerField(widget = forms.TextInput)
	paid = forms.BooleanField(widget = forms.CheckboxInput, required=False)

class UpdateQuantityForm(forms.Form):
	orderId = forms.IntegerField(widget = forms.TextInput)
	quantity = forms.IntegerField(widget = forms.TextInput)