# Generated by Django 5.0 on 2023-12-31 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_data_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 31, 7, 43, 8, 611723, tzinfo=datetime.timezone.utc)),
        ),
    ]
