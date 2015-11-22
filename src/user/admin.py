from django.contrib import admin

# Register your models here.

from .models import CreateAccount

class CreateAccountAdmin(admin.ModelAdmin):
	list_display = ["name", "id", "email", "is_staff"]
	class Meta:
		model = CreateAccount

admin.site.register(CreateAccount, CreateAccountAdmin)