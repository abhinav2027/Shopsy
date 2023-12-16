from django.shortcuts import render,redirect,HttpResponse
from store.models.cart import Cart

def checkout(request):
    context = {'cart_len' : len(Cart.objects.all())}
    return render(request,'store\checkout.html',context)