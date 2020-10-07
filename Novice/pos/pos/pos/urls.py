
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('customers/', include('customers.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('products/', include('products.urls')),
    path('sales/', include('sales.urls')),
    path('admin/', admin.site.urls),
]
