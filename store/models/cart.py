from django.db import models
from .product import Product


class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'