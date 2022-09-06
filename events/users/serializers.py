from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from django.db.models import Q
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
from eventlist.models import Event
from eventlist.serializers import EventSerializer


class UserSerializer(serializers.ModelSerializer):
    interested_events = serializers.SerializerMethodField('get_interested_events')

    def get_interested_events(self, instance):
        event_ids = instance.interested_events.all().values_list(
            'id', flat=True).distinct()
        events = []
        eventObjs = Event.objects.filter(id__in=event_ids)
        for eventobj in eventObjs:
            events.append(EventSerializer(eventobj).data)
        return events

    class Meta:
        model = User
        fields = ('id', 'email','password', 'city', 'interested_events')
        extra_kwargs = {
            
            "password": {

                
                'required': False,
                'write_only': True,
            },
        }

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password'])
        return super(UserSerializer, self).update(instance, validated_data)


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','password', 'interested_events', 'city')
        extra_kwargs = {
            "email": {
                'required': True,
                'allow_blank': False,
                'validators': [
                    EmailValidator
                ]
            },
            "password": {
                'write_only': True
            },
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(RegisterUserSerializer, self).create(validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, user_data):
        user_response = super(
            CustomTokenObtainPairSerializer, self).validate(user_data)

        # Access token with to include user detail.
        user_response.pop('refresh')
        user_response.update({
            "user": UserSerializer(self.user).data
        })

        return user_response

