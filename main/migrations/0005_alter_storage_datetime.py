# Generated by Django 4.2.7 on 2024-11-18 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_orders_orderer_remove_orders_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 18, 16, 0, 59, 938454)),
        ),
    ]