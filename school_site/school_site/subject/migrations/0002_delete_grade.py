# Generated by Django 4.2.5 on 2023-10-11 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0004_remove_student_absences_remove_student_grades_and_more"),
        ("subject", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Grade",
        ),
    ]
