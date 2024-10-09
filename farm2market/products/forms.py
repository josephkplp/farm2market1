from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Order, Review, Product

# Custom User Creation Form with validation
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if role not in ['farmer', 'customer']:  # You can add other roles here
            raise forms.ValidationError("Invalid role.")
        return role


# Unified Registration Form (DRY Principle)
class RegistrationForm(CustomUserCreationForm):
    pass  # Reusing the CustomUserCreationForm logic


# Enhanced Login Form with CAPTCHA (or rate limiting can be added)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password.")
            elif not user.is_active:
                raise forms.ValidationError("This account is inactive.")
        return cleaned_data


# Enhanced Profile Form to include Custom Fields
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Assuming CustomUser extends Django's User
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'bio']  # Adjust based on your CustomUser model

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered with another account.")
        return email


# Order Form with quantity validation
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'shipping_address']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get("product")
        quantity = cleaned_data.get("quantity")

        if product and quantity:
            if product.stock < quantity:
                raise forms.ValidationError(f"Only {product.stock} units of {product.name} are available.")
        return cleaned_data


# Review Form with rating validation
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating
