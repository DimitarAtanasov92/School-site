from django.db import models

from school_site.students.models import Teacher, Student


# Create your models here.


class SchoolClass(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
