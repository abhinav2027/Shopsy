from django.shortcuts import render,redirect,HttpResponseRedirect
from store.models.product import Product
from store.models.cart import Cart
from store.models.order import Order

def index(request):
    products = Product.objects.all()
    cart = Cart.objects.all()
    cart_len = len(cart)
    context = {'products' : products, 'cart_len' : cart_len}
    return render(request,'store\home.html',context)

