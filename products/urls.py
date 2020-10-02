from django.urls import path
from . import views

urlpatterns = [
	path('', views.index), # ITEMS # ITEMS # ITEMS
	path('input/', views.input),
	path('<id>/delete', views.delete),
	path('<id>/update', views.update),
	
	# path('category/category/', views.category), # CATEGORY # CATEGORY # CATEGORY
	# path('category/input_category/', views.input_category),
	# path('category/<id>/delete', views.delete_category),
	# path('category/<id>/update', views.update_category),
	# path('units/units/', views.units), # UNIT # UNIT # UNIT
	# path('units/input/', views.input_u),
	# path('units/<id>/delete', views.delete_u),
	# path('units/<id>/update', views.update_u),
]