from django.urls import path,include
from products import views

urlpatterns = [
    path('products/', views.products, name='products')
]