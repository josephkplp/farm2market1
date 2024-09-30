from . import views
from django.urls import path
from .views import (
    home,
    register,
    user_login,
    user_logout,
    profile,
    product_list,
    product_detail,
    cart,
    checkout,
    order_confirmation,
    order_history,
    search,
    page_not_found,
)




urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('order-history/', order_history, name='order_history'),
    path('search/', search, name='search'),
]

handler404 = page_not_found