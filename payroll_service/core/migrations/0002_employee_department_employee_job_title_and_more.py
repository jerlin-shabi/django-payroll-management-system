# Generated by Django 5.1.3 on 2024-11-11 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="department",
            field=models.CharField(default="HR", max_length=100),
        ),
        migrations.AddField(
            model_name="employee",
            name="job_title",
            field=models.CharField(default="HR", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="employee",
            name="salary",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Leave",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("leave_type", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[("approved", "Approved"), ("pending", "Pending")],
                        max_length=20,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.employee"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payroll",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "deductions",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("net_salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("month", models.CharField(max_length=20)),
                ("year", models.IntegerField()),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.employee"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Salary",
        ),
    ]