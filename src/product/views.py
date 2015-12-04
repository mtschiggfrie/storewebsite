from django.shortcuts import render
from .models import CreateProduct
from .forms import CreateProductForm
from .forms import SearchProductForm

# Create your views here.
def product(request):

	title = 'welcome'

	queryset = CreateProduct.objects.filter(active=True)
	form = SearchProductForm(request.POST or None)

	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
	}

	if 'order' in request.POST:
		queryset = CreateProduct.objects.order_by('price')
		context = {
			"title": 'Prices ordered',
			"queryset": queryset,
			"form": form,
		}
	
	if 'search' in request.POST:
		if form.is_valid():
			cd = form.cleaned_data
			a = cd.get('searchProduct')
			if cd.get('orderByPrice') == True:
				queryName = CreateProduct.objects.filter(name__contains=a).order_by('price')
				queryDescription = CreateProduct.objects.filter(description__contains=a).order_by('price')
			else:
				queryName = CreateProduct.objects.filter(name__contains=a)
				queryDescription = CreateProduct.objects.filter(description__contains=a)
				
			queryset = queryName | queryDescription
			context = {
				"title": "Search results for: " + a,
				"queryset": queryset,
				"form": form,
			}


	return render(request, "product.html", context)


def createproduct(request):
	title = 'Create a Product'
	form = CreateProductForm(request.POST or None)


	context = {
		"title": title,
		"form": form,
		
	}


	if form.is_valid():
		instance = form.save(commit=False)
		query = CreateProduct.objects.filter(name=instance.name).count()
		if query == 0:
			instance.save()
			context = {
				"title":  'Product Created Successfully'
			}
		else:
			context = {
				"title":  'Product Name already in use.'
			}


	return render(request, "createproduct.html", context)