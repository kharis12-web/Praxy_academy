from django.shortcuts import render, redirect
from . import models, forms

# VIEWS ITEM/INDEX # VIEWS ITEM/INDEX # VIEWS ITEM/INDEX
def index(req):
	prod = models.Prod.objects.all()
	return render(req, 'products/index.html', {
		'data' : prod,
		})

def input(req):
	form = forms.Prod()

	if req.POST:
		form = forms.Prod(req.POST)
		if form.is_valid():
			form.save()
		return redirect('/products')

	prod = models.Prod.objects.all()
	return render(req, 'products/input.html', {
		'data' : prod,
		'form' : form,
		})

def update(req, id):
	form = forms.Prod()

	if req.POST:
		form = forms.Prod(req.POST)
		if form.is_valid():
			form.update()
			form.save()
		return redirect('/products')
	# if req.POST:
	# 	models.Prod.objects.filter(pk=id).update(
	# 		kode = req.POST['kode'],
	# 		name = req.POST['name'],
	# 		price = req.POST['price'],
	# 		stok = req.POST['stok'])
	# 	return redirect('/products')

	prod = models.Prod.objects.filter(pk=id).first()
	return render(req, 'products/update.html', {
		'data' : prod,
		'form' : form,
		})

def delete(req, id):
	models.Prod.objects.filter(pk=id).delete()
	return redirect('/products')

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