from django.db import models

# Create your models here.

class CalendarFeed(models.Model):
    title=models.CharField(max_length=200)
    start=models.DateField()
    end=models.DateField(null=True,blank=True)
