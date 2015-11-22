from django.db import models

# Create your models here.
class CreateAccount(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	password = models.CharField(max_length = 25)
	email = models.EmailField()
	is_staff = models.BooleanField(default=False)


def __unicode__(self):
    return CreateAccount