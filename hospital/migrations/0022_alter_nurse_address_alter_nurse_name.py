# Generated by Django 4.1.12 on 2023-11-26 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0021_remove_nurse_user_nurse_address_nurse_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nurse", name="address", field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="nurse", name="name", field=models.CharField(max_length=20),
        ),
    ]
