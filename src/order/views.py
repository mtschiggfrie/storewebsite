from django.shortcuts import render
from product.models import CreateProduct
from .forms import ContainsForm
from .models import Contains
from .models import CreateOrder
from .models import Orders
from django.contrib.auth.models import User
from django.utils import timezone
from itertools import chain


# Create your views here.
def order(request, int):

	title = int
	queryset = CreateProduct.objects.get(id=int)
	#form = ContainsForm(request.POST or None)
	form = ContainsForm(request.POST or None, initial={'productId': int})
	

	context = {
		"form":form,
		"title": title,
		"queryset": queryset
	}

	if form.is_valid():
		createorder = CreateOrder()
		createorder.date = timezone.now()
		createorder.save()
		instance = form.save(commit=False)
		instance.orderId = createorder.OrderId
		instance.productId = int
		instance.save()
		order = Orders()
		order.userId = request.user.id
		order.orderId = createorder.OrderId
		order.save()
		context = {
			"title":  createorder.OrderId
	}


	return render(request, "order.html", context)


def cart(request):

	context = {
		"title": "error",
		"orders": {},
	}

	title = request.user.id
	#username = User.objects.get(email=instance.email)
	ordersQuery = Orders.objects.filter(userId=request.user.id).only()
	orders = list(ordersQuery)

	totals = []
	contains = []
	for order in orders:
		containsList = Contains.objects.filter(orderId=order.orderId)
		contains.extend(list(containsList))
		totals.extend(list(containsList.quantity))

	#list1 = list(set(orders)|set(contains))

	products = []
	index = 0
	for contain in contains:
		productsList = CreateProduct.objects.filter(id=contain.productId)
		products.extend(list(productsList))
		totals[index] = totals[index] * productsList.price



	context = {
		"title": title,
		"orders": orders,
		"contains": contains,
		"products": products,
		"totals": totals,
		#"list1": list1,
	}

	# try:
	# 	title = request.user.id
	# 	#username = User.objects.get(email=instance.email)
	# 	orders = Orders.objects.get(userId=request.user.id)

	# 	context = {
	# 		"title": title,
	# 		"orders": orders,
	# 	}
	# except: 
 #  		pass

	return render(request, "cart.html", context)