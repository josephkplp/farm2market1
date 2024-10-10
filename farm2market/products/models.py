from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



# Create your models here.

# User Model

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('customer', 'Customer'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    
    # Override the related_name for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this name to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username  # Use username for better representation
    
    #Product Model
    
class Product(models.Model):
    farmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)  # Add image field
    stock = models.PositiveIntegerField()  # Amount available
    created_at = models.DateTimeField(auto_now_add=True) # Add a default value
    updated_at = models.DateTimeField(auto_now=True)
        

    def __str__(self):
        return self.name

# Order Model

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ], default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True),
    shipping_address = models.CharField(max_length=255)  

    def save(self, *args, **kwargs):
        # Calculate the total price as product price * quantity
        self.total_price = self.product.price * self.quantity
        super(Order, self).save(*args, **kwargs)


    def __str__(self):
        return f"Order {self.id} by {self.customer.username}" #

#Review Model
 
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()  # Assume rating is out of 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField( auto_now_add=True) # Add a default value

    def __str__(self):
        return f"Review for {self.product.name} by {self.customer.username}"

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)  # Optional, track logged-in users
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the Product model
    quantity = models.IntegerField(default=1)  # Track quantity of the product
    added_on = models.DateTimeField(auto_now_add=True)  # Automatically add timestamp when the item is added
