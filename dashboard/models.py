from django.db import models
from account.models import CustomUser

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 200)
    price = models.IntegerField()
    image = models.ImageField(upload_to = "products")

class Orders(models.Model):
    ordered_by = models.ForeignKey(CustomUser, models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    ORDER_STATUS = (
        ("pending", "Pending"),
        ("delivered", "Delivered"),
        ("cancelled", "cancelled")
    )
    order_status = models.CharField(choices = ORDER_STATUS, max_length = 10)

