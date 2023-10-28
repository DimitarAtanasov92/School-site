from django.db import models
from django.db.models import CASCADE
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):

    email = models.EmailField(max_length=30)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    subject = models.ManyToManyField(Subject, blank=True, null=True)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
