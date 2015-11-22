from django.shortcuts import render
from .models import CreateProduct

# Create your views here.
def product(request):

	title = 'welcome'

	queryset = CreateProduct.objects.all()

	context = {
		"title": title,
		"queryset": queryset,
	}

	return render(request, "product.html", context)

