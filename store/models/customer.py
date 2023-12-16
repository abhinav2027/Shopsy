from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.PositiveIntegerField(max_length=10)

    def register(self):
        self.save()
    @staticmethod
    def retrieve_by_email(email):
        try:
            Customer.objects.filter(email = email)
        except:
            return False
    def if_exists(self):
        if Customer.objects.filer(email = self.email):
            return True
        else:
            return False



