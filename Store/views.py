from Store.models import Category, Products, Customer, Order
from django.contrib.auth.hashers import  check_password, make_password
from django.views import  View
from django.shortcuts import render , redirect , HttpResponseRedirect
 
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

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )
    



class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')




# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)




class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')





class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})




class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        firstName = postData.get('firstName')
        lastName = postData.get('lastName')
        phoneNumber_1 = postData.get('phoneNumber_1')
        phoneNumber_2 = postData.get('phoneNumber_2')
        country = postData.get('country')
        city = postData.get('city')
        address = postData.get('address')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'firstName': firstName,
            'lastName': lastName,
            'phoneNumber_1 ': phoneNumber_1,
            'phoneNumber_2': phoneNumber_2,
            'country': country,
            'city': city,
            'address': address,
            'email': email
        }
        error_message = None

        customer = Customer(firstName=firstName,
                            lastName=lastName,
                            phoneNumber_1=phoneNumber_1,
                            phoneNumber_2=phoneNumber_2,
                            country=country,
                            city=city,
                            email=email,
                            address=address,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(firstName, lastName, phoneNumber_1, phoneNumber_2, country, city, email, address, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.firstName:
            error_message = "Please Enter your First Name !!"
        elif len(customer.firstName) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.lastName:
            error_message = 'Please Enter your Last Name'
        elif len(customer.lastName) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phoneNumber_1:
            error_message = 'Enter your Phone Number'
        elif len(customer.phoneNumber_1) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message


