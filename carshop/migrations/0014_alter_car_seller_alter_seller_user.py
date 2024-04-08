# Generated by Django 4.2.6 on 2024-04-01 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("carshop", "0013_seller_car_seller"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="seller",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cars_sold",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="seller",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="seller_profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
