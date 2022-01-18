# Generated by Django 4.0.1 on 2022-01-15 17:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('positivenews', '0004_product_quantity_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='positivenews.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Quantity should be >= 0')]),
        ),
    ]
