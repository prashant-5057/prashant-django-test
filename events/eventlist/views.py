from django.shortcuts import render
from rest_framework import generics
from .serializers import EventSerializer
from rest_framework.response import Response
from .models import Event
from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class EventView(generics.GenericAPIView):
    """ Create API view for class "EventView" and "EventSerializer".
    This view verify all input and create new event """
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer

    def get(self, request, format=None):
        today = date.today()
        events = self.queryset.filter(event_date__gte=today)
        serializer = self.serializer_class(events, many=True)
        return Response({'data': serializer.data}, status=200)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=200)
        return Response({'error': serializer.errors}, status=400)


class InterestAddRemoveApi(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        is_interested = request.GET.get('is_interested')
        user = self.request.user
        event = Event.objects.filter(pk=pk)
        if not event.exists():
            return Response({'error': {"event_id": ["Please provide valid event id."]}}, status=400)

        user.interested_events.add(pk) if is_interested == 'true' else user.interested_events.remove(pk)
        serializer = EventSerializer(event.first())
        return Response({'status': True, 'id': pk, 'is_interested': is_interested, 'interested_event': serializer.data})