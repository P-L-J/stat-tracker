from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tracker.serializers import ActivitySerializer, StatSerializer
from tracker.models import Activity, Stat


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activities to be viewed or edited.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class StatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stats to be viewed or edited.
    """
    queryset = Stat.objects.all()
    serializer_class = StatSerializer