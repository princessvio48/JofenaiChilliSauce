from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import  check_password, make_password
from django.views import  View
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.core.cache import cache
from django.http import JsonResponse
from .forms import UserCreateForm
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()
    context = {'product':products, 'cartItems':cartItems}
    context = {'items':items, 'order':order, 'cartItems':cartItems,'product':products}
    return render(request, "store/index.html",context)
  


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password2']
        try:
            user = authenticate(username=User.objects.get(email=username), password=password)
        except:
            user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            #check if is super user
            if user.is_superuser:
                messages.success(request, f"You are now logged in as {username}")
                return redirect('/admin')
            else:
                messages.success(request, f"You are now logged in as {username}")
                return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
       
        
    
    return render(request, 'store/login.html')


def register(request):
    
    if request.method == 'POST':
        username = request.POST['username1']
        email = request.POST['email']
        phone_nummber = request.POST['phonenumber']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
    else:
        return render(request,'store/register.html')
   


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    cache.clear()
    return redirect("/")


@csrf_exempt
def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)



@csrf_exempt
def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

@csrf_exempt
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	# print('Action:', action)
	# print('Product:', productId)

	user = request.user
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(user=user, complete=False)

	orderItem, created = OrderProduct.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)

	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    reference = data['payment']['reference']
    # print("reference: ", reference)

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
    else:
        user, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    order.payment_reference = reference

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
        user=user,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)

def orderPlace(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    products = Product.objects.all()
   
    context = {'items':items, 'order':order, 'cartItems':cartItems,'product':products}
    return render(request, 'store/orderPlace.html',context)


def about(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()
    context = {'product':products, 'cartItems':cartItems}
    
    context = {'items':items, 'order':order, 'cartItems':cartItems,'product':products}
    return render(request, 'store/about_us.html',context)

def products(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()
    context = {'product':products, 'cartItems':cartItems}
    
    context = {'items':items, 'order':order, 'cartItems':cartItems,'product':products}
    return render(request, 'store/products.html',context)

def contact_us(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()
    context = {'product':products, 'cartItems':cartItems}
    
    context = {'items':items, 'order':order, 'cartItems':cartItems,'product':products}
    return render(request, 'store/contact_us.html',context)

