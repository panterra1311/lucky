from django_filters import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то что запросил пользователь
            'quantity': ['gt'],
            'date': ['gt'],
            'author': ['exact'],
            'category__name': ['contains'],# количество товаров должно быть больше или равно тому, что указал пользователь
            }