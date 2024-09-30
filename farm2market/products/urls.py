from . import views
from django.urls import path
from .views import register  # Adjust the import based on your view name




urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),  # View for creating new products (if needed)
    path('products/', views.product_list, name='product_list'),
    path('register/', register, name='register'),  # Add this line
    
]
