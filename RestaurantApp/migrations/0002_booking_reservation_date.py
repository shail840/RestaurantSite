# Generated by Django 4.1.4 on 2024-03-06 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]