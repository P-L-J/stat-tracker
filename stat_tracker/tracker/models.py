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
from faker import Faker
import random


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

    @classmethod
    def fake_stats(cls, num):
        """Generate up to num fake stats for each activity, skipping pre-existing dates"""
        activities = Activity.objects.all()

        fake = Faker()
        fake_date = lambda: fake.date_time_between(start_date="-30d",
                                                   end_date="now").date()

        for activity in activities:
            existing_dates = [stat.date for stat in activity.stat_set.all()]
            dates = sorted(
                set([fake_date() for _ in range(num)]).union(existing_dates))
            for date in dates:
                Stat.objects.create(date=date, activity=activity,
                                    value=random.randint(1, 20))
