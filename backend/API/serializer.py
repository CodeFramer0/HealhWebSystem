from rest_framework import serializers
from django.contrib.auth.models import User
from web_interface.models import Complaint,Organ

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Complaint
        fields = ['user', 'organ', 'title', 'description','date']

class OrganSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Organ
        fields = ['name']

