# Generated by Django 3.1.4 on 2021-01-26 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0029_auto_20210125_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
