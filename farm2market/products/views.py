from .models import Product
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


# Create your views here.
def index(request):
    return HttpResponse("hello world")

def new(request):
    return HttpResponse("new products")


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})