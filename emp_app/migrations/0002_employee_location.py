# Generated by Django 4.1.1 on 2022-09-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emp_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="location",
            field=models.CharField(default="Nepal", max_length=100),
        ),
    ]
