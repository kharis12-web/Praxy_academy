from django.shortcuts import render, redirect
from . import models, forms
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict

# VIEWS ITEM/INDEX # VIEWS ITEM/INDEX # VIEWS ITEM/INDEX
def index_py(req):
	# tasks = models.Prod.objects.filter(owner=req.user)
	prod = models.Prod.objects.all()
	form = forms.Prod()
	if req.POST:
		form = forms.Prod(req.POST)
		if form.is_valid():
			form.instance.owner = req.user
			form.save()
	return render(req, ('products/index.html'), {
		'data' : prod,
		# 'data': tasks, 
		'form': form,
		})

def index(req):
	prod = models.Prod.objects.all()
	print(prod)

	products = [] # merubah array versi django mjd array biasa
	for p in prod:
		products.append(model_to_dict(p))
	return JsonResponse({'data': products})


def category(req):
	cate = models.Cate.objects.all()

	kategori = [] # merubah array versi django mjd array biasa
	for p in cate:
		kategori.append(model_to_dict(p))
	return JsonResponse({'data': kategori})

def input(req):
	# tasks = models.Prod.objects.filter(owner=req.user)
	form = forms.Prod()
	if req.method == 'POST':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		cate = models.Cate.objects.filter(pk=data['cate']).first()
		form = forms.Prod(data)
		if form.is_valid():
			form.instance.cate = cate
			form.save()
	return JsonResponse({
		'data' : model_to_dict(form.instance),
		})
	
def input_c(req):
	# tasks = models.Cate.objects.filter(owner=req.user)
	form = forms.Cate()
	if req.method == 'POST':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		form = forms.Cate(data)
		print(data)
		if form.is_valid():
			form.save()
	return JsonResponse({
		'data' : model_to_dict(form.instance),
		})

def input_c_py(req):
	tasks = models.Cate.objects.filter(owner=req.user)
	form = forms.Cate()

	if req.POST:
		form = forms.Cate(req.POST)
		if form.is_valid():
			form.instance.owner =req.user
			form.save()
		return redirect('/products/category')
		
	cate = models.Cate.objects.all()
	return render(req, 'category/input_category.html', {
		'data' : cate,
		'form' : form,
		'data' : tasks,
		})

def category_py(req):
	tasks = models.Cate.objects.filter(owner=req.user)
	cate = models.Cate.objects.all()
	form = forms.Cate()
	if req.POST:
		form = forms.Cate(req.POST)
		if form.is_valid():
			form.instance.owner = req.user
			form.save()
	return render(req, ('category/category.html'), {
		'data1' : tasks,
		'form' : form,
		})

def update(req, id):
	# tasks = models.Prod.objects.filter(owner=req.user)
	form = forms.Prod()

	if req.POST:
		form = forms.Prod(req.POST)
		if form.is_valid():
			form.update()
			form.save()
		return redirect('/products')

	prod = models.Prod.objects.filter(pk=id).first()
	return render(req, 'products/update.html', {
		'data' : prod,
		'form' : form,
		'data' : tasks,
		})

def delete(req, id):
	delete = models.Prod.objects.filter(pk=id).delete()
	return JsonResponse({
		'data' : delete,
		})

def delete_c(req, id):
	delete = models.Cate.objects.filter(pk=id).delete()
	return JsonResponse({
		'data' : delete,
		})



		
# # VIEWS CATEGORY # VIEWS CATEGORY # VIEWS CATEGORY # VIEWS CATEGORY
# def category(req):
# 	cate = models.Cate.objects.all()
# 	return render(req, 'category/category.html', {
# 		'data' : cate,
# 		})

# def input_category(req):
# 	if req.POST:
# 		models.Cate.objects.create(
# 			name = req.POST['name'])
# 		return redirect('/category/category')

# 	cate = models.Cate.objects.all()
# 	return render(req, 'category/input_category.html', {
# 		'data' : cate,
# 		})

# def update_category(req, id):
# 	if req.POST:
# 		models.Cate.objects.filter(pk=id).update(
# 			name = req.POST['name'])
# 		return redirect('/category')

# 	cate = models.Cate.objects.filter(pk=id).first()
# 	return render(req, 'category/update_category.html', {
# 		'data' : cate,
# 		})

# def delete_category(req, id):
# 	models.Cate.objects.filter(pk=id).delete()
# 	return redirect('/category/category')

# # VIEWS UNITS # VIEWS UNITS # VIEWS UNITS
# def units(req):
# 	unit = models.Units.objects.all()
# 	return render(req, 'units/unit.html', {
# 		'data' : unit,
# 		})

# def input_u(req):
# 	if req.POST:
# 		models.Units.objects.create(
# 			name = req.POST['name'])
# 		return redirect('/units/units')

# 	unit = models.Units.objects.all()
# 	return render(req, 'units/input.html', {
# 		'data' : unit,
# 		})

# def update_u(req, id):
# 	if req.POST:
# 		models.Units.objects.filter(pk=id).update(
# 			name = req.POST['name'])
# 		return redirect('/units')

# 	unit = models.Units.objects.filter(pk=id).first()
# 	return render(req, 'units/update.html', {
# 		'data' : unit,
# 		})

# def delete_u(req, id):
# 	models.Units.objects.filter(pk=id).delete()
# 	return redirect('/units/units')