from django.shortcuts import render
from .models import Category, Products

# Create your views here.
def products(request):
    categorys = Category.objects.all()


    search = request.GET.get('search')
    category = request.GET.get('category')
    priceRange = request.GET.get('priceRange')

    if search != None:
        products = Products.objects.filter(name__icontains=search)

    elif category != None:
        products = Products.objects.filter(category__name=category)

    elif priceRange != None:
        if priceRange == 'low-to-high':
            products = Products.objects.filter().order_by('price')
        else:
            products = Products.objects.filter().order_by('-price')

    elif category and priceRange != None:
        if priceRange == 'low-to-high':
            products = Products.objects.filter(category__name=category).order_by('price')
        else:
            products = Products.objects.filter(category__name=category).order_by('-price')
        
    else:
        products = Products.objects.all()


    context = {
        'categorys':categorys,
        'products':products
    }
    return render(request, 'products/products.html', context)
