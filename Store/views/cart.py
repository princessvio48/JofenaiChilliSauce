from django.shortcuts import render , redirect
from Store.models import Category, Products, Customer, Order

from django.contrib.auth.hashers import  check_password
from django.views import  View
class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

