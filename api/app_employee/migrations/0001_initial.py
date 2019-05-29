# Generated by Django 2.2.1 on 2019-05-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=128)),
                ("department", models.CharField(max_length=255)),
            ],
            options={"verbose_name": "Employee", "verbose_name_plural": "Employees"},
        )
    ]
