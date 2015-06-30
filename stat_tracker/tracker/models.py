from django.db import models
# from django.utils import timezone
from datetime import datetime

"""
Activity:
    id
    title
Stat:
    id
    date
    activity FK
    value
"""


class Activity(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

class Stat(models.Model):
    date = models.DateField(default=datetime.today)
    activity = models.ForeignKey(Activity)
    value = models.IntegerField()

    def __str__(self):
        return '{}:{} @ {}'.format(self.activity, self.value, self.date)