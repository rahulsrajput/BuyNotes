from django.urls import path,include
from . import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('payment-success/', views.paymentSuccess, name='paymentSuccess'),
]