from django.db import models
from .category import Category

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField(default='',blank=True,null=True)
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/products/')
    size = models.CharField(max_length=4,default='')
    @staticmethod
    def retrieve_by_id(ids):
        return Product.objects.filter(id__in = ids)
    @staticmethod
    def retrieve_all_products():
        return Product.objects.all()
    @staticmethod
    def retireve_by_cat(cat_id):
        if cat_id:
            return Product.objects.filter(category = cat_id)
        else:
            return Product.retrieve_all_products()
    


