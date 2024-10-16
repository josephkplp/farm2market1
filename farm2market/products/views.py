from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, Product, Order, Review
from django.http import HttpResponse
from .models import Product,Cart
from .forms import CustomUserCreationForm, RegistrationForm, LoginForm, ProfileForm, OrderForm, ReviewForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


# Home View
def home(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'home.html', {'products': products})

# Registration View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required  # This decorator ensures that only logged-in users can access the profile@login_required  # This decorator ensures that only logged-in users can access the profile
# Profile View
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

# Product List View
def product_list(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'product_list.html', {'products': products})


# Product Detail View
def product_detail(request, product_id):
    # Retrieve the product or return a 404 if not found
    product = get_object_or_404(Product, id=product_id)

    # Handle review submission
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            # Create a review but don't save it yet
            review = review_form.save(commit=False)
            review.product = product
            review.customer = request.user  # Assuming request.user is the logged-in user
            review.save()  # Save the review to the database
            messages.success(request, 'Review submitted successfully!')  # Show success message
            
            # Redirect to the same product detail page
            return redirect('product_detail', product_id=product.id)
    else:
        review_form = ReviewForm()  # Create an empty review form for GET requests

    # Render the product detail page with the product and review form
    return render(request, 'product_details.html', {'product': product, 'review_form': review_form})

# Cart View
@login_required 
def cart(request):
    cart_items =  Cart.objects.filter(user=request.user)  # Your logic to get the cart items
    for item in cart_items:
        item.total_price = item.product.price * item.quantity  # Calculate total price

    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)
# Checkout View
def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            request.session['cart'] = {}  # Clear cart after order
            return redirect('order_confirmation', order.id)
    else:
        form = OrderForm()
    return render(request, 'checkout.html', {'form': form})

# Order Confirmation View
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})

# Order History View
def order_history(request):
    orders = Order.objects.filter(customer=request.user)  # Get user's orders
    return render(request, 'order_history.html', {'orders': orders})

# Search View
def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query)  # Search for products
    return render(request, 'search.html', {'results': results, 'query': query})

# 404 View
def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')