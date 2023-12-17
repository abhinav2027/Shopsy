from django.shortcuts import render,redirect,HttpResponse
from store.models.product import Product
from store.models.cart import Cart
import simplejson


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
        price = cart_item.product.price * cart_item.quantity
        items = Cart.objects.all()
        total_price = sum(item.product.price * item.quantity for item in items)
        total_quantity = sum(item.quantity for item in items)

        # print('success')
        return HttpResponse(simplejson.dumps({'quantity' : cart_item.quantity , 'price' : price, 'total_price' : total_price, 'total_quantity' : total_quantity, 'cart_len' : len(items)}),content_type='application/json')

    
def remove_cart(request):
    if request.method == 'GET':
        pid = request.GET['product_id']
        cart_item = Cart.objects.get(product_id = pid)
        if cart_item.quantity == 1:
            cart_item.delete()
            items = Cart.objects.all()
            total_price = sum(item.product.price * item.quantity for item in items)
            total_quantity = sum(item.quantity for item in items)
            return HttpResponse(simplejson.dumps({'quantity' : -1 , 'total_price' : total_price, 'total_quantity' : total_quantity, 'cart_len' : len(items)}),content_type='application/json')
        else:
            cart_item.quantity -= 1
            cart_item.save()
            items = Cart.objects.all()
            
            total_price = sum(item.product.price * item.quantity for item in items)
            total_quantity = sum(item.quantity for item in items)

            # print(type(cart_item.quantity))
            
            price = cart_item.product.price * cart_item.quantity
            
            # print('success')
            return HttpResponse(simplejson.dumps({'quantity' : cart_item.quantity , 'price' : price, 'total_price' : total_price, 'total_quantity' : total_quantity, 'cart_len' : len(items)}),content_type='application/json')

