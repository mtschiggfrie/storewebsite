from django.shortcuts import render
from product.models import CreateProduct
from .forms import ContainsForm
from .forms import PayForm
from .forms import DeleteCartForm
from .models import Contains
from .models import CreateOrder
from .models import Orders
from django.contrib.auth.models import User
from django.utils import timezone
from itertools import chain


# Create your views here.
def order(request, int):

	title = "Enter the amount of this product you would like to order."
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
			"title":  "Thank you. Your order has been placed inside your shopping cart."
	}


	return render(request, "order.html", context)


def cart(request):

	context = {
		"title": "error",
		"orders": {},
	}

	title = "Pay for your current order."
	#username = User.objects.get(email=instance.email)
	createOrderQuery = CreateOrder.objects.filter(paid=False)
	ordersQuery = Orders.objects.filter(userId=request.user.id, orderId__in=createOrderQuery).only()
	orders = list(ordersQuery)

	contains = []
	quantity = []
	for order in orders:
		containsList = Contains.objects.filter(orderId=order.orderId)
		contains.extend(list(containsList))
		quantity.extend(list(containsList.values('quantity') ))

	#list1 = list(set(orders)|set(contains))

	products = []
	price = []
	index = 0
	for contain in contains:
		productsList = CreateProduct.objects.filter(id=contain.productId)
		products.extend(list(productsList))
		price.extend(list(productsList.values('price')))
		index = index + 1

	totals = []
	total = 0

	for i in range(0, index):
		current = price[i]['price'] * quantity[i]['quantity']
		totals.append(current)
		total = total + current

	form = PayForm(request.POST or None, initial={'total': total})

	deletecartform = DeleteCartForm(request.POST or None)

	context = {
		"title": title,
		"orders": orders,
		"contains": contains,
		"products": products,
		"totals": totals,
		"total": total,
		"form": form,
		"deletecartform": deletecartform,

	}


	if 'pay' in request.POST:
		if form.is_valid():
			ids = Orders.objects.filter(userId=request.user.id, orderId__in=createOrderQuery).values_list('orderId', flat=True)
			var = CreateOrder.objects.filter(OrderId__in=ids, paid=False).count()
			#CreateOrder.objects.filter(OrderId__in=ids, paid=False).update(paid=True)


			for i in range(0, var):
				ids2 = Contains.objects.filter(orderId=orders[i].orderId)
				currentOrderID = ids2[0].orderId
				query = CreateProduct.objects.filter(id=ids2[0].productId).values_list('stock', flat=True)
				if (query[0]-quantity[i]['quantity']) < 0:
					context = {
						"title": 'We currently do not have that many in stock. Please try placing your order again.'
					}
					CreateOrder.objects.filter(OrderId=currentOrderID, paid=False).delete()
					Contains.objects.filter(orderId=currentOrderID).delete()
					Orders.objects.filter(orderId=currentOrderID).delete()
				else:
					CreateProduct.objects.filter(id=ids2[0].productId).update(stock=query[0]-quantity[i]['quantity'])
					context = {"title": "You paid for your orders successfully."}
					CreateOrder.objects.filter(OrderId=currentOrderID, paid=False).update(paid=True)


	if 'delete' in request.POST:
		if deletecartform.is_valid():
			cd = deletecartform.cleaned_data
			orderId = cd.get('orderId')
			CreateOrder.objects.filter(OrderId=orderId, paid=False).delete()
			Contains.objects.filter(orderId=orderId).delete()
			Orders.objects.filter(orderId=orderId).delete()


	
	return render(request, "cart.html", context)