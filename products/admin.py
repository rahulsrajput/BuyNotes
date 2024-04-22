from django.contrib import admin
from .models import Category, Products
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['uuid','name','created_at']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'price', 'discount']