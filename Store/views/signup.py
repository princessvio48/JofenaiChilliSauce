from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from Store.models import Category, Products, Customer, Order
from django.views import View


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
