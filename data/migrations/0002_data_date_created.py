# Generated by Django 5.0 on 2023-12-24 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 14, 30, 53, 340577, tzinfo=datetime.timezone.utc)),
        ),
    ]
