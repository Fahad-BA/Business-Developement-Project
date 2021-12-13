# Generated by Django 3.1.7 on 2021-04-08 20:46

from django.db import migrations, models
import logistic.models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0010_orders_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='City',
            field=models.CharField(choices=[('R', 'Riyadh.'), ('K', 'Kharj.'), ('J', 'Jeddah.'), ('M', 'Medina.'), ('D', 'Dammam.'), ('Kh', 'Khobar.')], default=logistic.models.City, max_length=50),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Pickup_Location',
            field=models.CharField(choices=[('R', 'Riyadhs office'), ('W', 'West offices'), ('E', 'East Offices'), ('D', 'Home Delivery')], default=logistic.models.Pick, max_length=50),
        ),
    ]