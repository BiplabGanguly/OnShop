from django.db import models
from users.models import User

class Product(models.Model):
    p_name = models.CharField(max_length=255)
    p_price = models.CharField(max_length=255)
    p_category = models.CharField(max_length=255)
    p_desc = models.TextField()
    p_quantity = models.CharField(max_length=255)
    p_img = models.FileField(upload_to="")

    def __str__(self):
        return self.p_name


class Wishlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)
    product_category = models.CharField(max_length=255)
    p_img = models.FileField(upload_to="wishlist/")

    def __str__(self):
        return self.user_id.first_name


