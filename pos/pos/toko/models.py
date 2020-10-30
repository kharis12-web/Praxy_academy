from django.db import models
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.db.models.fields.files import ImageFieldFile
class Toko(models.Model):
    pemilik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='toko')
    nama = models.CharField(default='', max_length=20)
    alamat = models.CharField(default='', max_length=100)
    telp = models.CharField(default='',max_length=15)
    gambar = models.TextField(default='')
