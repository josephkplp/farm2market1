from .models import CustomUser, Product, Order, Review
from django.contrib import admin

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Review)