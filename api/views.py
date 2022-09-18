from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import render
from .serializers import PassengerSerializers, PassengerTripSerializers
from primary.models import Passenger, PassengerTrip
from primary.tasks import send_email_task


class PassengerView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers
    def send_email(self):
        send_email_task(self.PassengerTrip.PassengerID.Name, self.Passenger.Trip.PassengerID.Email, self.Distance, (self.DestinationLatitude, self.DestinationLongitude))


class PassengerSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers
    lookup_field = 'id'


class TripView(generics.ListCreateAPIView):
    queryset = PassengerTrip.objects.all()
    serializer_class = PassengerTripSerializers

    def send_email(self):
        return send_email_task(self.PassengerTrip.PassengerID.Name, self.Passenger.Trip.PassengerID.Email, self.Distance, (self.DestinationLatitude, self.DestinationLongitude))


class TripSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PassengerTrip.objects.all()
    serializer_class = PassengerTripSerializers
    lookup_field = 'id'

