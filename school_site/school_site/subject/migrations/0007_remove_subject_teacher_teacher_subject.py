# Generated by Django 4.2.5 on 2023-11-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subject", "0006_remove_teacher_subject_subject_teacher"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subject",
            name="teacher",
        ),
        migrations.AddField(
            model_name="teacher",
            name="subject",
            field=models.ManyToManyField(blank=True, null=True, to="subject.subject"),
        ),
    ]
