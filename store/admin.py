from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

#this class is made to display the the object to real name 
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','catgory']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']

# Register your models here to edit it in admin site 
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order)
