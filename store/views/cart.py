from django.shortcuts import render,redirect,HttpResponse
from store.models.product import Product
from store.models.cart import Cart


def cart(request):
    cart = Cart.objects.all()
    cart_len = len(cart)
    quantity = sum(item.quantity for item in cart)    
    product_price = [item.quantity*item.product.price for item in cart]
    cart_items = zip(cart,product_price)
    price = sum(item.quantity*item.product.price for item in cart)
    context = {'items' : cart_items, 'quantity' : quantity, 'price' : price, 'product_price' : product_price, 'cart_len' : cart_len}
    # context = {}
    return render(request,'store\cart.html',context)

def add_cart(request):
    if request.method == 'GET':
        # print('yyy')
        pid = request.GET['product_id']
        product = Product.objects.get(pk = pid)
        cart_item, created = Cart.objects.get_or_create(product = product)
        cart_item.quantity += 1
        cart_item.save()
        return HttpResponse('Added : ' + str(cart_item.quantity))
    
def remove_cart(request):
    if request.method == 'GET':
        pid = request.GET['product_id']
        cart_item = Cart.objects.get(product_id = pid)
        cart_item.quantity += 1
        cart_item.save()
        print('success')
        return HttpResponse(cart_item.quantity)

