from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Product
from django.forms import Form, CharField, IntegerField, EmailField


class ProductForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity', 'description',
                  'check_box']  # не забываем включить галочку в поля иначе она не будет показываться на странице!

    class DummyForm(Form):
        field1 = CharField()
        field2 = IntegerField()
        field3 = EmailField()