from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)  # имя товара
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')])  # количество товара на складе
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # поле категории будет ссылаться на модель категории
    author = models.CharField(max_length=200, default="Default value")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.quantity}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/products/{self.id}'

# категории товаров: именно на них ссылается модель товара
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.name}'