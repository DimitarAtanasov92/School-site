# Generated by Django 4.2.5 on 2023-10-01 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SchoolClass",
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
                ("name", models.CharField(max_length=255)),
                ("students", models.ManyToManyField(to="students.student")),
                (
                    "teacher",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.teacher",
                    ),
                ),
            ],
        ),
    ]
