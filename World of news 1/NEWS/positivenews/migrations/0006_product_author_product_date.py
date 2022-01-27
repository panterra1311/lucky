# Generated by Django 4.0.1 on 2022-01-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positivenews', '0005_remove_product_author_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='Default value', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
