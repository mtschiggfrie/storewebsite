from django.db import models

# Create your models here.
class CreateOrder(models.Model):
	OrderId = models.AutoField(primary_key=True)
	date = models.DateField()
	paid = models.BooleanField(default=False)

class Orders(models.Model):
	userId = models.IntegerField()
	orderId = models.IntegerField()

class Contains(models.Model):
	orderId = models.IntegerField()
	productId = models.IntegerField()
	quantity = models.IntegerField()