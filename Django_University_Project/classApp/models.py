from django.db import models

class djangoClasses (models.Model):
    title = models.CharField(max_length=255)
    coursenumber = models.IntegerField()
    instructorname = models.CharField(max_length=255)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title