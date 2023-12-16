from django.contrib import admin
from .models import customer,category,order,product,cart

admin.site.register(customer.Customer)
admin.site.register(category.Category)
admin.site.register(order.Order)
admin.site.register(product.Product)
admin.site.register(cart.Cart)

# Register your models here.
