from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tracker.models import Activity, Stat


class StatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stat
        fields = ('url', 'date', 'activity', 'value')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    stat_set = StatSerializer(many=True, read_only=True)  # A nested list of 'stat' items.

    class Meta:
        model = Activity
        fields = ('url', 'title', 'stat_set')