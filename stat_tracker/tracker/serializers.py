from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tracker.models import Activity, Stat


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        # fields = ('',)


class StatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stat
        # fields = ('',)