# Generated by Django 3.1.4 on 2021-01-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0030_remove_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='order_product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=5, null=True),
        ),
    ]