
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()

IS_FOR_CHOICES = (
    (1, "Sale"),
    (2, "Buy"),
    (3, "To Rent"), #wish house to take rent if available
    (4, "For Rent") #house for give rent by owner
)


# model for the house ...
class Renthouse(models.Model):

    added_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Renthouse')
    title = models.CharField(max_length=250)
    descrption = models.TextField()
    location = models.CharField(max_length=250)

    land_area = models.FloatField(null=True, blank=True)
    floor_area =  models.FloatField(null=True, blank=True)
    bedroom = models.IntegerField(null=True, blank=True)
    bathroom = models.IntegerField(null=True, blank=True)

    livingroom = models.IntegerField(null=True, blank=True)
    kitchen = models.IntegerField(null=True, blank=True)
    room_details  = models.TextField(null=True, blank=True)
    furnished_condition = models.CharField(max_length=250,null=True, blank=True)

    built_year = models.DateField(null=True, blank=True)
    parking_sapce = models.CharField(max_length=300,null=True, blank=True)
    garden = models.CharField(max_length=10,null=True, blank=True)
    house_facing = models.CharField(max_length=300,null=True, blank=True)

    road_size = models.FloatField(null=True, blank=True)
    road_condition = models.CharField(max_length=250,null=True, blank=True)
    water_facilities = models.CharField(max_length=250,null=True, blank=True)
    sewage_facilties = models.CharField(max_length=250,null=True, blank=True)

    created_on = models.DateTimeField(default=timezone.now)
    is_for = models.IntegerField(choices=IS_FOR_CHOICES, default=1)

    def __str__(self):
        return self.title


class Renthouseimage(models.Model):
    image = models.ImageField(upload_to='house_picture')
    Renthouse = models.ForeignKey(Renthouse, on_delete=models.CASCADE, null=True, related_name='image')

    def __str__(self):
        return self.Renthouse.title
        

