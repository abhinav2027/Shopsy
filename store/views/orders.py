from django.shortcuts import render,redirect,HttpResponse

def orders(reqeust):
    return render(reqeust,'store\orders.html')

