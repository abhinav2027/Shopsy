from django.db import models
from .customer import Customer
from .product import Product
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    address = models.TextField(default='',blank=True)
    phone = models.PositiveIntegerField(max_length=10)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def place_order(self):
        self.save()
    @staticmethod
    def retrieve_orders_by_cust(cust_id):
        return Order.objects.filter(customer = cust_id).order_by('-date')


