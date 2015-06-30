from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
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

class StatListCreateView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StatSerializer

    def initial(self, request, *args, **kwargs):
        self.activity = Activity.objects.get(pk=kwargs['activity_pk'])
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return self.activity.stat_set.all()

    def perform_create(self, serializer):
        # if self.request.user != self.contact.owner:
        #     raise PermissionDenied
        serializer.save(activity=self.activity)

# class PhoneListCreateView(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = PhoneSerializer
#
#     def initial(self, request, *args, **kwargs):
#         self.contact = Contact.objects.get(pk=kwargs['contact_pk'])
#         super().initial(request, *args, **kwargs)
#
#     def get_queryset(self):
#         return self.contact.phones.all()
#
#     def perform_create(self, serializer):
#         if self.request.user != self.contact.owner:
#             raise PermissionDenied
#         serializer.save(contact=self.contact)
#         #contact = activity
#         #phone = stat