from django.shortcuts import render
from .models import Supplier
from .models import Supplys
from product.models import CreateProduct
from user.models import CreateAccount


# Create your views here.
def supply(request):

	supplierquery = Supplier.objects.all()
	supplysquery = Supplys.objects.all()

	

	context = {
		"supplierquery": supplierquery,
		"supplysquery": supplysquery,
		
	}



	return render(request, "supply.html", context)


def alert(request):

	lowproductsquery = CreateProduct.objects.filter(stock__lte=10)

	productsList = list(lowproductsquery)

	staffusers = CreateAccount.objects.filter(is_staff=True)

	suppliersList = []
	
	for obj in productsList:
		supplys = Supplys.objects.get(productId=obj.id)
		supplier = Supplier.objects.filter(id=supplys.supplierId)
		suppliersList.extend(list(supplier))


	context = {
		"title": "This is a list of all products low on stock.",
		"productsList": productsList,
		"suppliersList": suppliersList,
		"staffusers": staffusers
	}

	return render(request, "alert.html", context)