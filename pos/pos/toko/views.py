from django.shortcuts import render
from . import models, forms
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from pos.auth import check_token

def index(req):
	token_data = check_token(req.META['HTTP_AUTHORIZATION'])
	if not(token_data['id']):
		return JsonResponse({ 'error': 'akses tidak diizinkan' }, status=401)

	toko = models.Toko.objects.all()
	datatoko = []

	for t in toko:
		datatoko.append(model_to_dict(t))
	return JsonResponse({'toko' : datatoko,})

def create(req):
	# tasks = models.Prod.objects.filter(owner=req.user)
	form = forms.Toko()
	if req.method == 'POST':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		form = forms.Toko(data)
		if form.is_valid():
			form.save()
	return JsonResponse({
		'datatoko' : model_to_dict(form.instance),
		})

def delete(req, id):
	delete = models.Toko.objects.filter(pk=id).delete()
	return JsonResponse({
		'toko' : delete,
		})

def pembeli(req):
	toko = models.Toko.objects.all()
	datatoko = []

	for t in toko:
		datatoko.append(model_to_dict(t))
	return JsonResponse({'toko' : datatoko,})







	
