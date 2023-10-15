from django.db import models
from django.db.models import CASCADE
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Teacher(models.Model):
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


class Subject(models.Model):
    teachers = models.ForeignKey(Teacher, on_delete=CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

