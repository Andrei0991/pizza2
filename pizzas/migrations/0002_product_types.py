# Generated by Django 3.1.4 on 2021-01-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='types',
            field=models.CharField(choices=[('Neapolitan Pizza', 'Neapolitan Pizza'), ('Chicago Pizza', 'Chicago Pizza'), ('New York-Style Pizza', 'New York-Style Pizza'), ('Greek Pizza', 'Greek Pizza'), ('California Pizza', 'California Pizza'), ('Capricciosa Pizza', 'Capricciosa Pizza'), ('Mexicana Pizza', 'Mexicana Pizza'), ('Quattro Stagioni Pizza', 'Quattro Stagioni Pizza')], max_length=255, null=True),
        ),
    ]