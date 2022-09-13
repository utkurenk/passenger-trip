from django.db import models


class Passenger(models.Model):
    Name = models.CharField()
    eMail = models.EmailField()
    Address = models.CharField()
    Country = models.CharField()
    City = models.CharField()


class PassengerTrip(models.Model):
    totalDistance = models.PositiveIntegerField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    passengerID = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=True)
