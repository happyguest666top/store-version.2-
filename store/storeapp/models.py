from django.db import models
from django.contrib.auth.models import AbstractUser


class Category (models.Model):
    title = models.CharField(max_length=180)

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    title = models.CharField(max_length=180)
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.title}, {self.phone_number}, {self.address}"


class Product(models.Model):
    title = models.CharField(max_length=180)
    price = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="images/products", verbose_name="photo")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}, {self.price}, {self.description}, {self.photo}, {self.category}, {self.manufacturer}"


class Client(AbstractUser):
    birthday = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=25)
    favourite_post = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}, {self.birthday}, {self.phone_number}, {self.favourite_post}, {self.product}"


class Order (models.Model):

    STATUS_CHOICES = [
        ("incart", "В корзині"),
        ("new", "Нове"),
        ("processing", "В обробці"),
        ("sent", "Відправлено"),
        ("completed", "Завершено"),
        ("cancelled", "Скасовано"),
    ]
    client = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    def __str__(self):
        return f"order number: {self.id}"


class Order_product (models.Model):
    amount = models.CharField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.amount}, {self.product}, {self.order}"



