from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=80)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

#for email validation 
    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
