from django.db import models

# Create your models here.
class Supplier(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField()

class Supplys(models.Model):
	supplierId = models.IntegerField()
	productId = models.IntegerField()