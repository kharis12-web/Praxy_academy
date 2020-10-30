from django.db import models
from datetime import datetime
from products import models as products_models
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
# Create your models here.
class Sale(models.Model):
	# owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name='sale')
	date = models.DateField(default=datetime.now)

	# def ____(self):
	# 	return self.date

	def total(self):
		details = SaleDetail.objects.filter(sale=self.id)
		total_price = 0
		for detail in details:
			total_price += detail.total()
		return total_price
	
class SaleDetail(models.Model):	
	sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sama')
	products = models.ForeignKey(products_models.Prod, on_delete=models.CASCADE, related_name='terjual')
	qty = models.PositiveSmallIntegerField(default=0)
	desc =models.TextField(default='',max_length= 50)

	def __repr__(self):
		return '{} {} {}'.format(self.products, self.qty, self.products.stok)
		
	def total(self):
		return self.qty*self.products.price

	def stok(self):
		return self.products.stok-self.qty


