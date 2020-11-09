from django.shortcuts import render, redirect
from . import models, forms
from toko import models as toko_models
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from pos.auth import check_token

def index(req):
	token_data = check_token(req.META['HTTP_AUTHORIZATION'])
	if not(token_data['id']):
		return JsonResponse({ 'error': 'akses tidak diizinkan' }, status=401)

	
	toko = toko_models.Toko.objects.filter(pemilik=token_data['id']).first()
	prod = models.Prod.objects.filter(toko =toko)
	print(prod)

	products = [] # merubah array versi django mjd array biasa
	for p in prod:
		products.append(model_to_dict(p))
	return JsonResponse({'data': products})


def category(req):
	token_data = check_token(req.META['HTTP_AUTHORIZATION'])
	if not(token_data['id']):
		return JsonResponse({ 'error': 'akses tidak diizinkan' }, status=401)
	
	toko = toko_models.Toko.objects.filter(pemilik=token_data['id']).first()
	cate = models.Cate.objects.filter(toko=toko)

	kategori = [] # merubah array versi django mjd array biasa
	for p in cate:
		kategori.append(model_to_dict(p))
	return JsonResponse({'data': kategori})

def input(req):
	token_data = check_token(req.META['HTTP_AUTHORIZATION'])
	if not(token_data['id']):
		return JsonResponse({ 'error': 'akses tidak diizinkan' }, status=401)
		

	toko = toko_models.Toko.objects.filter(pemilik=token_data['id']).first()
	form = forms.Prod()
	if req.method == 'POST':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		cate = models.Cate.objects.filter(pk=data['cate']).first()

		print(data)
		form = forms.Prod(data)
		if form.is_valid():
			form.instance.cate = cate
			form.instance.toko = toko
			prod = form.save()
			return JsonResponse({
				'data' : model_to_dict(prod),
				# 'data1': tasks,
				})
		else:
			return JsonResponse({ 'error': form.errors }, status=401)
	return JsonResponse({ 'error': 'akses tidak diizinkan' }, status=401)
	
def input_c(req):
	token_data = check_token(req.META['HTTP_AUTHORIZATION'])
	if not(token_data['id']):
		return JsonResponse({ 'error': 'akses tidak diizinkan' }, status=401)

	toko = toko_models.Toko.objects.filter(pemilik=token_data['id']).first()
	form = forms.Cate()
	if req.method == 'POST':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		form = forms.Cate(data)
		print(data)
		if form.is_valid():
			form.instance.toko = toko
			form.save()
	return JsonResponse({
		'data' : model_to_dict(form.instance),
		# 'data1': tasks,
		})

def update(req, id):
	if req.method == 'PUT':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		put=models.Prod.objects.filter(pk=id).first()
		models.Prod.objects.filter(pk=id).update(
			cate = models.Cate.objects.filter(pk=data['cate']).first() if 'cate' in data else put.cate,
			kode = data['kode'] if 'kode' in data else put.kode,
			name = data['name'] if 'name' in data else put.name,
			price = data['price'] if 'price' in data else put.price,
			stok = data['stok'] if 'stok' in data else put.stok,
			image = data['image'] if 'image' in data else put.image,
			deskp = data['deskp'] if 'deskp' in data else put.deskp,
		)
		put=models.Prod.objects.filter(pk=id).first()
		return JsonResponse({
			'data' : model_to_dict(put),
			})	
	return JsonResponse({ 'error': 'akses tidak diizinkan' }, status=401)


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