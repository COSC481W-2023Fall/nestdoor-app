from tkinter import NO
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.detail}"
    
# MAIN DISCUSSIONS
# MAIN DISCUSSIONS
# MAIN DISCUSSIONS
    
class Post(models.Model):
    # main
    post_id = models.AutoField(primary_key=True)
    datetime_posted = models.DateTimeField()
    posted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    number_replies = models.IntegerField()
    datetime_last_edited = models.DateTimeField(null=True)
    
    # moderation
    datetime_last_moderated = models.DateTimeField(null=True)
    last_moderated_by = models(User, null=True, on_delete=models.SET_NULL)
    moderated_note = models.TextField()

class Reply(models.Model):
    # main
    reply_id = models.AutoField(primary_key=True)
    for_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    for_reply_id = models.ForeignKey('self', on_delete=models.CASCADE)
    datetime_posted = models.DateTimeField()
    posted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    datetime_last_edited = models.DateTimeField(null=True)
    
    # moderation
    datetime_last_moderated = models.DateTimeField(null=True)
    last_moderated_by = models(User, null=True, on_delete=models.SET_NULL)
    moderated_note = models.TextField()
    
# FOR BUILDINGS
# FOR BUILDINGS
# FOR BUILDINGS
    
class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    datetime_added = models.DateTimeField()
    number_mentions = models.IntegerField()
    address = models.TextField()
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    
class BuildingPost(models.Model):  # many to many linking table for when posts mention buildings
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    
class BuildingReply(models.Model): # many to many linking table for when replies mention buildings
    id = models.AutoField(primary_key=True)
    reply_id = models.ForeignKey(Reply, on_delete=models.CASCADE)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    
class Location(models.Model): # locations within buildings
    location_id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(Building, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    datetime_added = models.DateTimeField()
    number_mentions = models.IntegerField()
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    description = models.TextField()
    
    # check constraint that either the building or the longitude and latitude must be set
    def clean(self):
        super().clean()
        if self.building_id is None and (self.gps_longitude is None or self.gps_latitude is None):
            raise ValidationError('Either the building or gps coordinates must be specified.')
        
    class Meta:
        db_constraints = {
            'location_building_or_gps_coords': 'CHECK (building_id IS NOT NULL OR (gps_longitude IS NOT NULL AND gps_latitude IS NOT NULL))',
        }

class LocationPost(models.Model):  # many to many linking table for when posts mention locations
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    
class LocationReply(models.Model): # many to many linking table for when replies mention locations
    id = models.AutoField(primary_key=True)
    reply_id = models.ForeignKey(Reply, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)