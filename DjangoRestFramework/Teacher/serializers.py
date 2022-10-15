from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from Teacher.models import Teacher


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Teacher
        fields = ['url', 'username', 'email', 'group']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']