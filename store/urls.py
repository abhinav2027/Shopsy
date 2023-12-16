from django.contrib import admin
from django.urls import path
from .views.home import index
from .views.cart import cart,add_cart,remove_cart
from .views.checkout import checkout
from .views.orders import orders
from .views.login import login
from .views.signup import signup
from .views.category import men_category,women_category,electronics
from .views.detail import detail
from django.conf import settings
from django.conf.urls.static import static 

 
urlpatterns = [
    path('', index, name='homepage'),
    path('cart', cart, name='cart'),
    path('check-out',checkout, name='checkout'),
    path('orders',orders, name='orders'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('mens-clothing',men_category,name='mensclothing'),
    path('womens-clothing',women_category,name='womensclothing'),
    path('electronics',electronics,name='electronics'),
    path('<id>/detail/',detail,name='detail'),
    path('add-cart/',add_cart,name='add_cart'),
    path('update-cart',remove_cart,name='update-cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)