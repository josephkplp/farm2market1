from .models import CustomUser, Product, Order, Review,Cart
from django.contrib import admin

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Cart)