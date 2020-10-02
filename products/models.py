from django.db import models

# Create your models here.
class Prod(models.Model):
	kode = models.CharField(max_length=10)
	name = models.CharField(max_length=10)
	price = models.IntegerField(default=0)
	stok = models.IntegerField(default=0)

	def __str__(self):
		return "{} - {}".format(self.kode, self.name)

class Cate(models.Model):
	name = models.TextField(default='')

class Units(models.Model):
	name = models.TextField(default='')
