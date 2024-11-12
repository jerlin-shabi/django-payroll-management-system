# Generated by Django 5.1.3 on 2024-11-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leave_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaverequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Denied", "Denied"),
                ],
                default="Pending",
                max_length=50,
            ),
        ),
    ]