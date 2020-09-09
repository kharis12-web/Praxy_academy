from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('task/', include('task.urls')),
    path('suplayer/', include('suplayer.urls')),
    path('cabang/', include('cabang.urls')),
    path('', include('home.urls')),
]


