# Generated by Django 4.1.12 on 2023-11-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0022_alter_nurse_address_alter_nurse_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="room_num",
            field=models.CharField(max_length=10, null=True),
        ),
    ]