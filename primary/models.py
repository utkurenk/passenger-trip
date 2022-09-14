from django.db import models


class Passenger(models.Model):
    Name = models.CharField(max_length=60)
    Email = models.EmailField(max_length=30)
    Country = models.CharField(max_length=60)
    City = models.CharField(max_length=60)
    TotalDistanceCovered = models.IntegerField(default=0)
    HomeLatitude = models.DecimalField(max_digits=12, decimal_places=10)
    HomeLongitude = models.DecimalField(max_digits=12, decimal_places=10)


class PassengerTrip(models.Model):
    CreatedAt = models.DateTimeField(auto_now_add=True)
    DestinationLatitude = models.DecimalField(max_digits=12, decimal_places=10)
    DestinationLongitude = models.DecimalField(max_digits=12, decimal_places=10)
    PassengerID = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=True)
