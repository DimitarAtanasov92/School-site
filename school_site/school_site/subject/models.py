from django.db import models
# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Grade(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(choices=[(i, i) for i in range(1, 7)])
    date = models.DateField()

    def __str__(self):
        return f"{self.subject} - Grade: {self.grade}"
