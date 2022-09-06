from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from django.db.models import Q
from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = "__all__"


#class Rateserializer(serializers.ModelSerializer):

#    class Meta:
#       model = Event
#       fields = ""
        



