from django.shortcuts import render, redirect
from . import models, forms

# VIEWS ITEM/INDEX # VIEWS ITEM/INDEX # VIEWS ITEM/INDEX
def index(req):
	tasks = models.Prod.objects.filter(owner=req.user)
	prod = models.Prod.objects.all()
	form = forms.Prod()
	if req.POST:
		form = forms.Prod(req.POST)
		if form.is_valid():
			form.instance.owner = req.user
			form.save()
	return render(req, ('products/index.html'), {
		'data' : prod,
		'data': tasks, 
		'form': form,
		})

def category(req):
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

# def input(req):
# 	tasks = models.Prod.objects.filter(owner=req.user)
# 	form = forms.Prod()
# 	if req.POST:
# 		form = forms.Prod(req.POST)
# 		if form.is_valid():
# 			form.instance.owner =req.user
# 			form.save()
# 		return redirect('/products')

	# prod = models.Prod.objects.all()
	# return render(req, 'products/input.html', {
	# 	'data' : prod,
	# 	'form' : form,
	# 	'data': tasks,
	# 	})

def input_c(req):
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

def update(req, id):
	tasks = models.Prod.objects.filter(owner=req.user)
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
	models.Prod.objects.filter(pk=id).delete()
	return redirect('/products')

def delete_c(req, id):
	models.Cate.objects.filter(pk=id).delete()
	return redirect('/products/category')
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