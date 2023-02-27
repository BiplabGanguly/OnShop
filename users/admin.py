from django.contrib import admin
from users.models import Profile,State
from products.models import Product,Wishlist
# Register your models here.
admin.site.register(Profile)
admin.site.register(State)
admin.site.register(Product)
admin.site.register(Wishlist)
