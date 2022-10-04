from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('login', views.login_request, name = 'login'),
	path('register', views.register, name = 'register'),
	path('logout', views.logout_request, name = 'logout'),
 	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
 	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	
 
]