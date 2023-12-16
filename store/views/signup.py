from django.shortcuts import render
from store.models.cart import Cart

def signup(request):
    context = {'cart_len' : len(Cart.objects.all())}
    return render(request,'store/signup.html',context)