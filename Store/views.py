from django.shortcuts import render , redirect
from Store.models import Category, Products, Customer, Order

from django.contrib.auth.hashers import  check_password
from django.views import  View

def remove(self, product):
   
    # Remove a product from the cart.
    product_id = str(product.id)
    if product_id in self.cart:
        # Subtract 1 from the quantity
        self.cart[product_id]['quantity'] -= 1
        # If the quantity is now 0, then delete the item
        if self.cart[product_id]['quantity'] == 0:
            del self.cart[product_id]
        self.save()