# Generated by Django 4.2.2 on 2023-06-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="phone",
            field=models.CharField(max_length=200),
        ),
    ]
