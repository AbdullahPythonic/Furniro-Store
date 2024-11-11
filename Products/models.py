from django.db import models
from Categories.models import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=450)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.name
