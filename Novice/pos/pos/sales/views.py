from django.shortcuts import render,redirect

from customers import models as customers_models
# from product import models as product_models
from . import models, forms
# Create your views here.
def index(req):
	tasks = models.Sale.objects.filter(owner=req.user)
	form = forms.SalesForm()
	if req.POST:
		form = forms.SalesForm(req.POST)
		if form.is_valid():
			form.instance.owner = req.user
			form.save()
		return redirect('/sales')
	sale = models.Sale.objects.all()
	return render(req, ('sales/index.html'), {
		'data' : sale,
		'form' : form,
		'data' : tasks,
		})

def transaksi(req):
	tasks = models.Sale.objects.filter(owner=req.user)
	sale = models.Sale.objects.all()
	total =0
	for p in sale:
		total+=p.total()

	return render(req, ('transaksi/list_transaksi.html'), {
		'data' : sale,
		'total': total,
		'data' : tasks,
		})

def input(req):
	tasks = models.Sale.objects.filter(owner=req.user)
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

def print(req):
	print = models.Sale.objects.all()
	return render(req, ('sales/print.html'), {
		'data' : print,
		})
	
def delete(req, id):
	models.Sale.objects.filter(pk=id).delete()
	return redirect('/sales')

def detail(req, id):
    sale = models.Sale.objects.filter(pk=id).all()
    return render(req, 'sales/detail.html', {
        'data': sale,
    })

