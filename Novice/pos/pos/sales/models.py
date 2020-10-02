from django.db import models
from datetime import datetime
from products import models as products_models
from django.contrib.auth.models import User
# Create your models here.
class Sale(models.Model):
	owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name='sale')
	date = models.DateField(default=datetime.now)
	products = models.ForeignKey(products_models.Prod, on_delete=models.CASCADE, related_name='terjual')
	qty = models.PositiveSmallIntegerField(default=0)
	desc =models.TextField(default='')

	def __repr__(self):
		return self.products, self.date, self.qty, self.products.stok
		
	def total(self):
		return self.qty*self.products.price

	def stok(self):
		return self.products.stok-self.qty


