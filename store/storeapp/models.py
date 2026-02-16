from django.db import models

class Category (models.Model):
    title = models.CharField(max_length=180)

    def __str__(self):
        return self.title

class Manufacturer (models.Model):
    title = models.CharField(max_length=180)
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.title}, {self.phone_number}, {self.address}"

class Product (models.Model):
    title = models.CharField(max_length=180)
    price = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="images/products", verbose_name="photo")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)

