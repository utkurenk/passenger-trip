# from django.contrib.gis.db import models
from django.db import models
import geopy.distance
from .tasks import send_email_task


class Passenger(models.Model):
    Name = models.CharField(max_length=60)
    Email = models.EmailField(max_length=30)
    Country = models.CharField(max_length=60)
    City = models.CharField(max_length=60)
    HomeLatitude = models.DecimalField(max_digits=9, decimal_places=6)
    HomeLongitude = models.DecimalField(max_digits=9, decimal_places=6)


class PassengerTrip(models.Model):
    CreatedAt = models.DateTimeField(auto_now_add=True)
    PassengerID = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=True)
    DestinationLatitude = models.DecimalField(max_digits=9, decimal_places=6)
    DestinationLongitude = models.DecimalField(max_digits=9, decimal_places=6)
    Distance = models.IntegerField(blank=True, default=0)

    def calculate_distance(self):
        coords_1 = (self.PassengerID.HomeLatitude, self.PassengerID.HomeLongitude)
        coords_2 = (self.DestinationLatitude, self.DestinationLongitude)
        return round(geopy.distance.geodesic(coords_1, coords_2).km)

    def save(self,*args, **kwargs):
        self.Distance = self.calculate_distance()
        return super(PassengerTrip, self).save(*args, **kwargs)

    def send_email(self):
        send_email_task(self.PassengerID.Name, self.PassengerID.Email, self.Distance, (self.DestinationLatitude, self.DestinationLongitude))

