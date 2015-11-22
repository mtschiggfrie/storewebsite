from django.contrib import admin

# Register your models here.

from .models import CreateProduct

class CreateProductAdmin(admin.ModelAdmin):
	list_display = ["name", "id", "price", "stock", "active"]
	class Meta:
		model = CreateProduct

admin.site.register(CreateProduct, CreateProductAdmin)