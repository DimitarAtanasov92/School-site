from django.db import models
from django.db.models import CASCADE

from school_site.school_class.models import SchoolClass
from school_site.subject.models import Subject
from school_site.auth_teachers.models import AppUser
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Student(models.Model):
    email = models.EmailField(max_length=30)
    name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, blank=True, null=True)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Note(models.Model):
    text = models.TextField()
    date = models.DateField()
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=CASCADE)

    def __str__(self):
        return self.text


class Absence(models.Model):
    absences = models.IntegerField()
    date = models.DateField()
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=CASCADE)

    def __str__(self):
        return f"Absences: {self.absences}"


class Grade(models.Model):
    subject = models.ManyToManyField(Subject, null=True, blank=True)
    grade = models.IntegerField(choices=[(i, i) for i in range(1, 7)])
    date = models.DateField()
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} - Grade: {self.grade}"
