from rest_framework import serializers
from primary.models import Passenger, PassengerTrip


class PassengerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class PassengerTripSerializers(serializers.ModelSerializer):
    class Meta:
        model = PassengerTrip
        fields = '__all__'