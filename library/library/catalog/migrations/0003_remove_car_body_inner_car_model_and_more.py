# Generated by Django 4.0.5 on 2022-06-02 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_car_brand_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_body',
            name='inner_car_model',
        ),
        migrations.DeleteModel(
            name='inner_car_model',
        ),
    ]
