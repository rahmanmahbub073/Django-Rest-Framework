from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from .serializers import TeacherSerializer, GroupSerializer
from rest_framework import permissions
# Create your views here.


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
