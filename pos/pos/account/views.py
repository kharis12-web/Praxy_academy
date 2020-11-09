from django.db import models
from django.shortcuts import render, redirect 
from django.http import JsonResponse, HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from pos.auth import create_token, check_token
from .models import *
from .forms import CreateUserForm
from toko.forms import CreateTokoForm

def registerPage(req):
	if req.method == 'POST':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)

		user_input = data['user']
		toko_input = data['toko']
		user_input['password1'] = user_input['password']
		user_input['password2'] = user_input['password']
		form = CreateUserForm(user_input)

		if form.is_valid():
			user = form.save()

			form_toko = CreateTokoForm(toko_input)
			if form_toko.is_valid():
				form_toko.instance.pemilik = user
				toko = form_toko.save()
				return JsonResponse({ 'user': model_to_dict(user), 'toko': model_to_dict(toko) })
			return JsonResponse({ 'user': model_to_dict(user), 'toko': 'gagal membuat toko' })
		else:
			print(form.errors)
			return JsonResponse({ 'error': form.errors }, status=401)

	return JsonResponse({ 'error': 'akses tidak diizinkan' }, status=401)

def loginPage(request):
	if request.method == 'POST':
		data_byte = request.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)

		username = data['username']
		password = data['password']

		user = User.objects.filter(username=username).first()
		response = {}
		if user:
			is_password_valid = user.check_password(password)

			if is_password_valid:
				token_data = {
					'id': user.id,
					'username': user.username,
				}
				token = create_token(token_data)
				response['token'] = token
				return JsonResponse(response)
			else:
				response['error'] = 'Password Yang Anda Masukan Salah'
				return JsonResponse(response, status=400)
		else:
			response['error'] = 'username belum terdaftar'
			return JsonResponse(response, status=400)
		

	return JsonResponse({ 'error': 'akses tidak diizinkan' }, status=401)
def logoutUser(request):
	logout(request)
	return redirect('/account/')
