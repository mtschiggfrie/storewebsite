from django.contrib import admin

# Register your models here.
from .models import CreateOrder
from .models import Orders
from .models import Contains

class CreateOrderAdmin(admin.ModelAdmin):
	list_display = ["OrderId", "date", "paid"]
	class Meta:
		model = CreateOrder

class OrdersAdmin(admin.ModelAdmin):
	list_display = ["userId", "orderId"]
	class Meta:
		model = Orders

class ContainsAdmin(admin.ModelAdmin):
	list_display = ["orderId", "productId", "quantity"]
	class Meta:
		model = Contains

admin.site.register(CreateOrder, CreateOrderAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Contains, ContainsAdmin)