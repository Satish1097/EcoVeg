from django.contrib import admin
from .models import Customer,ProductCategory,Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(ProductCategory)
admin.site.register(Product)