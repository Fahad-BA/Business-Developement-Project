# Generated by Django 3.1.7 on 2021-04-08 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0005_auto_20210408_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='logistic.orders'),
            preserve_default=False,
        ),
    ]
