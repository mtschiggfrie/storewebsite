from django.shortcuts import render
from .forms import DeleteProductForm
from .forms import UpdateProductForm
from .forms import ProductLookUpForm
from .forms import DeleteUserForm
from .forms import UserLookUpForm
from .forms import UpdateUserForm
from .forms import UpdateQuantityForm
from .forms import DeleteOrderForm
from .forms import ChangePaidForm
from user.forms import CreateAccountForm
from product.forms import CreateProductForm
from product.models import CreateProduct
from user.models import CreateAccount
from order.models import Contains
from order.models import Orders
from order.models import CreateOrder
from supply.models import Supplier
from supply.models import Supplys
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
import datetime



# Create your views here.
def home(request):
	return render(request, "home.html", {})

#@staff_member_required
def manage(request):
	return render(request, "manage.html", {})

def users(request):
	queryset = CreateAccount.objects.all()
	deleteform = DeleteUserForm(request.POST or None)
	lookupform = UserLookUpForm(request.POST or None)
	updateform = UpdateUserForm(request.POST or None, initial={'is_staff': False})
	createform = CreateAccountForm(request.POST or None)
	context = {
		"deleteform": deleteform,
		"queryset": queryset,
		"updateform": updateform,
		"lookupform": lookupform,
		"createform": createform,

	}

	if 'delete' in request.POST:
		if deleteform.is_valid():
			cd = deleteform.cleaned_data
			a = cd.get('deleteUser')
			CreateAccount.objects.filter(id=a).delete()
			context = {
				"deleteform": DeleteUserForm(request.POST or None),
				"queryset": queryset,
				"updateform": updateform,
				"lookupform": lookupform,
				"createform": createform,

			}

	if 'lookup' in request.POST:
		if lookupform.is_valid():
			cd = lookupform.cleaned_data
			a = cd.get('UserId')
			if CreateAccount.objects.filter(id=a).exists():
				obj = CreateAccount.objects.get(id=a)
				updateform = UpdateUserForm(initial={'id': a, 'name': obj.name, 'address': obj.address, 'password': obj.password, 'email': obj.email, 'is_staff': obj.is_staff})
				context = {
					"deleteform": deleteform,
					"queryset": queryset,
					"updateform": updateform,
					"lookupform": UserLookUpForm(request.POST or None),
					"createform": createform,

				}

	if 'update' in request.POST:
		if updateform.is_valid():
			cd = updateform.cleaned_data
			q = CreateAccount.objects.get(id=cd.get('id'))
			email = q.email
			beforeStaff = q.is_staff
			CreateAccount.objects.filter(id=cd.get('id')).update(name=cd.get('name'), address=cd.get('address'), password=cd.get('password'), email=cd.get('email'), is_staff=cd.get('is_staff'))
			afterStaff = cd.get('is_staff')

			if beforeStaff == True and afterStaff == False:
				User.objects.get(email=email).delete()
				User.objects.create_user(cd.get('name'), cd.get('email'), cd.get('password'))

			if beforeStaff == False and afterStaff == True:
				User.objects.get(email=email).delete()
				User.objects.create_superuser(cd.get('name'), cd.get('email'), cd.get('password'))

			context = {
				"deleteform": deleteform,
				"queryset": queryset,
				"updateform": UpdateUserForm(request.POST or None, initial={'is_staff': False}),
				"lookupform": lookupform,
				"createform": createform,

			}

	if 'create' in request.POST:
		if createform.is_valid():
			instance = createform.save(commit=False)
			instance.save()

			context = {
				"deleteform": deleteform,
				"queryset": queryset,
				"updateform": updateform,
				"lookupform": lookupform,
				"createform": CreateAccountForm(request.POST or None),

			}


	return render(request, "manageusers.html", context)

def orders(request):
	createorderquery = CreateOrder.objects.all()
	ordersquery = Orders.objects.all()
	containsquery = Contains.objects.all()
	deleteorderform = DeleteOrderForm(request.POST or None)
	updatequantityform = UpdateQuantityForm(request.POST or None)
	changepaidform = ChangePaidForm(request.POST or None)

	context = {
		"createorderquery": createorderquery,
		"ordersquery": ordersquery,
		"containsquery": containsquery,
		"deleteorderform": deleteorderform,
		"updatequantityform": updatequantityform,
		"changepaidform": changepaidform,

	}

	if 'changepaid' in request.POST:
		if changepaidform.is_valid():
			cd = changepaidform.cleaned_data
			CreateOrder.objects.filter(OrderId=cd.get('orderId')).update(paid=cd.get('paid'))


	if 'updatequantity' in request.POST:
		if updatequantityform.is_valid():
			cd = updatequantityform.cleaned_data
			Contains.objects.filter(orderId=cd.get('orderId')).update(quantity=cd.get('quantity'))

	if 'delete' in request.POST:
		if deleteorderform.is_valid():
			cd = deleteorderform.cleaned_data
			a = cd.get('deleteOrder')
			CreateOrder.objects.filter(OrderId=a).delete()
			Contains.objects.filter(orderId=a).delete()
			Orders.objects.filter(orderId=a).delete()

	return render(request, "manageorders.html", context)

def products(request):
	queryset = CreateProduct.objects.all()
	deleteform = DeleteProductForm(request.POST or None)
	lookupform = ProductLookUpForm(request.POST or None)
	updateform = UpdateProductForm(request.POST or None)
	createform = CreateProductForm(request.POST or None)
	context = {
		"deleteform": deleteform,
		"queryset": queryset,
		"updateform": updateform,
		"lookupform": lookupform,
		"createform": createform,

	}

	if 'delete' in request.POST:
		if deleteform.is_valid():
			cd = deleteform.cleaned_data
			a = cd.get('deleteProduct')

			#need to make sure not used in last 30 days
			ContainsProductToDeleteQuery = Contains.objects.filter(orderId=a)
			LatestDate = CreateOrder.objects.filter(OrderId__in=ContainsProductToDeleteQuery).latest('date')
			DaysSinceLastOrder = datetime.date.today() - LatestDate.date

			if DaysSinceLastOrder.days < 30:
				CreateProduct.objects.filter(id=a).delete()
				context = {
					"deleteform": DeleteProductForm(request.POST or None),
					"queryset": queryset,
					"updateform": updateform,
					"lookupform": lookupform,
					"createform": createform,

				}

	if 'lookup' in request.POST:
		if lookupform.is_valid():
			cd = lookupform.cleaned_data
			a = cd.get('ProductId')
			if CreateProduct.objects.filter(id=a).exists():
				obj = CreateProduct.objects.get(id=a)
				updateform = UpdateProductForm(initial={'id': a, 'name': obj.name, 'price': obj.price, 'stock': obj.stock, 'description': obj.description, 'active': obj.active})
				context = {
					"deleteform": deleteform,
					"queryset": queryset,
					"updateform": updateform,
					"lookupform": ProductLookUpForm(request.POST or None),
					"createform": createform,

				}

	if 'update' in request.POST:
		if updateform.is_valid():
			cd = updateform.cleaned_data
			CreateProduct.objects.filter(id=cd.get('id')).update(name=cd.get('name'), price=cd.get('price'), stock=cd.get('stock'), description=cd.get('description'), active=cd.get('active'))
			context = {
				"deleteform": deleteform,
				"queryset": queryset,
				"updateform": UpdateProductForm(request.POST or None),
				"lookupform": lookupform,
				"createform": createform,

			}

	if 'create' in request.POST:
		if createform.is_valid():
			instance = createform.cleaned_data
			query = CreateProduct.objects.filter(name=instance.get('name')).count()
			if query == 0:
				entry = CreateProduct(name=instance.get('name'), price=instance.get('price'), stock=instance.get('stock'), description=instance.get('description'), active=instance.get('active'))
				entry.save()
				doesSupplierExist = Supplier.objects.filter(name=instance.get('supplier')).count()
				if doesSupplierExist > 0:
					supplierquery = Supplier.objects.get(name=instance.get('supplier'))
					addSupplys = Supplys(supplierId=supplierquery.id , productId=entry.id)
					addSupplys.save()
				else:
					newSupplier = Supplier(name=instance.get('supplier'))
					newSupplier.save()
					newSupplys = Supplys(supplierId=newSupplier.id , productId=entry.id)
					newSupplys.save()

			context = {
				"deleteform": deleteform,
				"queryset": queryset,
				"updateform": updateform,
				"lookupform": lookupform,
				"createform": CreateProductForm(request.POST or None),

			}


			

	return render(request, "manageproducts.html", context)