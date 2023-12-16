from django.shortcuts import render
from store.models.product import Product
from store.models.cart import Cart


def detail(reqeust,id):
    product = Product.objects.get(pk = id)

    context = {'product' : product, 'cart_len' : len(Cart.objects.all())}
    return render(reqeust,'store\detail.html',context)