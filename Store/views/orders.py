from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from Store.models import Category,Products, Customer,Order
from django.views import View


class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
