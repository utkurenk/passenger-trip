from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import render
from .serializers import PassengerSerializers, PassengerTripSerializers
from primary.models import Passenger, PassengerTrip


class PassengerView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers


class PassengerSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers
    lookup_field = 'id'


class TripView(generics.ListCreateAPIView):
    queryset = PassengerTrip.objects.all()
    serializer_class = PassengerTripSerializers


class TripSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PassengerTrip.objects.all()
    serializer_class = PassengerTripSerializers
    lookup_field = 'id'

