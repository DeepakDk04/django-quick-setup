from django.contrib import admin

from .models import Product, Account, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Account)
admin.site.register(Category)