from django.shortcuts import render,redirect
from products import models as products_models
from . import models, forms
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
# Create your views here.
def index(req):
	# sales = models.Sale.objects.filter(owner=req.user)
	form = forms.SalesForm()
	saledetail=models.SaleDetail.objects.all()
	if req.POST:
		form = forms.SalesForm(req.POST)
		if form.is_valid():
			form.instance.owner = req.user
			sale = form.save()
			return redirect('/sales/{}'.format(sale.id))
	return render(req, ('sales/index.html'), {
		# 'data1' : sales,
		'form' : form,
		'detail' : saledetail,
		})

def index(req):
	sale_detail = models.SaleDetail.objects.all()

	sale_detail = [] # merubah array versi django mjd array biasa
	for p in sale_detail:
		sale_detail.append(model_to_dict(p))
	return JsonResponse({'data': sale_detail})

def sale_detail(req, id):
	# tasks = models.Sale.objects.filter(owner=req.user)
	form = forms.SaleDetail()
	salebyid=models.Sale.objects.filter(pk=id).first()
	if req.POST:
		form = forms.SaleDetail(req.POST)
		if form.is_valid():
			form.instance.sale = salebyid
			# form.instance.owner = req.user
			sale=form.save()
			stok_baru = sale.products.stok-sale.qty
			products_models.Prod.objects.filter(pk=sale.products.id).update(stok=stok_baru)
	saledetail=models.SaleDetail.objects.filter(sale=salebyid)
	total=0
	for t in saledetail:
		total+=t.total()
	return render(req, ('sales/input_detail.html'),{
		'data':saledetail,
		'form':form,
		'total':total,
		'sale':salebyid,
	})

def transaksi(req):
	# tasks = models.Sale.objects.filter(owner=req.user)
	sale = models.Sale.objects.all()
	total =0
	for p in sale:
		total+=p.total()

	return render(req, ('transaksi/list_transaksi.html'), {
		'data' : sale,
		'total': total,
		# 'data' : tasks,
		})

def input(req):
	# tasks = models.Sale.objects.filter(owner=req.user)
	form = forms.SalesForm()

	if req.POST:
		form = forms.SalesForm(req.POST)
		if form.is_valid():
			form.instance.owner = req.user
			form.save()
		
		return redirect('/sales')

	sale = models.Sale.objects.all()
	return render(req, ('sales/input.html'), {
		'data' : sale,
		'form' : form,
		'data' : tasks,
		})

def cetak(req):
	print = models.Sale.objects.all()
	return render(req, ('sales/print.html'), {
		'data' : print,
		})
	
def delete(req, id):
	models.Sale.objects.filter(pk=id).delete()
	return redirect('/sales')

def detail(req, id):
	sale = models.Sale.objects.filter(pk=id).first()
	saledetail=models.SaleDetail.objects.filter(sale=sale)
	return render(req, 'sales/detail.html', {
		'data': sale,
		'datadetail': saledetail,
		})

def delete_detail(req,id,id_detail):
	models.SaleDetail.objects.filter(pk=id_detail).delete()
	# stok_detail = products.stok+qty
	# products_models.Prod.objects.filter(pk=sale.products.id).update(stok=stok_detail)
	return redirect(f'/sales/{id}/detail')

