from django.shortcuts import render
from store.models.cart import Cart


def login(request):
    context = {'cart_len' : len(Cart.objects.all())}
    return render(request,'store\login.html',context)