from django.db import models

from school_site.subject.models import Grade, Subject


class Note(models.Model):
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.text


class Absence(models.Model):
    absences = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Absences: {self.absences}"


class Student(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    grades = models.ManyToManyField(Grade)
    absences = models.ManyToManyField(Absence)
    notes = models.ManyToManyField(Note)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Teacher(models.Model):
    subjects = models.ManyToManyField(Subject)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

