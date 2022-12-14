from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('login', views.login_request, name = 'login'),
	path('register', views.register, name = 'register'),
	path('logout', views.logout_request, name = 'logout'),
	path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
 	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('order', views.orderPlace, name='order'),
 	path('about', views.about, name='about'),
 	path('contact_us', views.contact_us, name='contact_us'),
 	path('products', views.products, name='products'),
 
]