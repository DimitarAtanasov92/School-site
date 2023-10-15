from django.db import models

from school_site.subject.models import Teacher


# Create your models here.


class SchoolClass(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
