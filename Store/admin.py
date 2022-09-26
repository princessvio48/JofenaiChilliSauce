from django.contrib import admin
from .models import *


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    #fields = ['retail', 'order_date','order_status','complete']
    list_display = ('user','date_ordered','order_status','complete',)
class OrderProductAdmin(admin.ModelAdmin):
    #fields = ['retail', 'order_date','order_status','complete']
    list_display = ('product','order','quantity','created_at','updated_at')
class ProductAdmin(admin.ModelAdmin):
    #fields = ['retail', 'order_date','order_status','complete']
    list_display = ('name','price','category','description','image')
class ShippingAddressAdmin(admin.ModelAdmin):
    #fields = ['retail', 'order_date','order_status','complete']
    list_display = ('user','order','address','city','state','zipcode','date_added')
    
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
