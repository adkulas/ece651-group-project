# Generated by Django 2.1.7 on 2019-03-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_doctor",
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_patient",
            field=models.NullBooleanField(default=False),
        ),
    ]
