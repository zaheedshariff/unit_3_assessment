from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    person = models.CharField(max_length=100)

    # def __str__(self):
        # return f"{self.get_description_display()} on {self.time}"
    class Meta:
        ordering = ['-time']
