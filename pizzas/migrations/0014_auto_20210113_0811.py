# Generated by Django 3.1.4 on 2021-01-13 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0013_auto_20210112_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
