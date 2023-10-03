from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to="event_img", blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


