from django.shortcuts import render
from store.models.product import Product
from store.models.cart import Cart

def men_category(request):
    products = Product.objects.filter(category_id = 1)
    cart_len = len(Cart.objects.all())
    context = {'products' : products, 'cart_len' : cart_len}

    return render(request,'store/home.html',context)

def women_category(request):
    products = Product.objects.filter(category_id = 2)
    cart_len = len(Cart.objects.all())
    context = {'products' : products, 'cart_len' : cart_len}
    return render(request,'store/home.html',context)

def electronics(request):
    products = Product.objects.filter(category_id = 3)
    cart_len = len(Cart.objects.all())
    context = {'products' : products, 'cart_len' : cart_len}
    return render(request,'store/home.html',context)

