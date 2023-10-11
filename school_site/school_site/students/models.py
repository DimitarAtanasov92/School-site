from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import CASCADE

from school_site.subject.models import Subject
from school_site.auth_teachers.models import AppUser

UserModel = get_user_model()


class Student(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

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


class Teacher(models.Model):
    subjects = models.ManyToManyField(Subject)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    is_teacher = models.BooleanField(default=False)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Grade(models.Model):

    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(choices=[(i, i) for i in range(1, 7)])
    date = models.DateField()
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=CASCADE)

    def __str__(self):
        return f"{self.subject} - Grade: {self.grade}"

