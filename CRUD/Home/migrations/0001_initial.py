# Generated by Django 5.0.1 on 2024-01-16 11:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "ID",
                    models.CharField(max_length=16, primary_key=True, serialize=False),
                ),
                ("Name", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="Employe",
            fields=[
                (
                    "ID",
                    models.CharField(max_length=16, primary_key=True, serialize=False),
                ),
                ("Name", models.CharField(max_length=32)),
                ("Department", models.CharField(max_length=32)),
            ],
        ),
    ]