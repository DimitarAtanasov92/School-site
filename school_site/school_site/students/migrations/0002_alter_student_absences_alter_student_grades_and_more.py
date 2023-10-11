# Generated by Django 4.2.5 on 2023-10-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subject", "0001_initial"),
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="absences",
            field=models.ManyToManyField(blank=True, null=True, to="students.absence"),
        ),
        migrations.AlterField(
            model_name="student",
            name="grades",
            field=models.ManyToManyField(blank=True, null=True, to="subject.grade"),
        ),
        migrations.AlterField(
            model_name="student",
            name="notes",
            field=models.ManyToManyField(blank=True, null=True, to="students.note"),
        ),
    ]