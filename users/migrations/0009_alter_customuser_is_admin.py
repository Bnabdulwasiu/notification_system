# Generated by Django 5.0 on 2023-12-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
