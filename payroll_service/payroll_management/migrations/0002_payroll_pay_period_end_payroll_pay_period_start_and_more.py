# Generated by Django 5.1.3 on 2024-11-12 08:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payroll_management", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payroll",
            name="pay_period_end",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="payroll",
            name="pay_period_start",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="payroll",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Paid", "Paid"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
    ]