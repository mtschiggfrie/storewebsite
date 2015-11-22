from django.db import models

# Create your models here.
class CreateProduct(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	price = models.IntegerField()
	stock = models.IntegerField()
	description = models.TextField()
	active = models.BooleanField(default=True)
