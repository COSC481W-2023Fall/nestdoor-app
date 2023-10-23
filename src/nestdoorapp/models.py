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
      

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    addr = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name} {self.detail}"
        return f"{self.first_name} {self.last_name}"
    
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

    # check constraint that a post contains content
    def clean(self):
        super().clean()
        if self.content is None:
            raise ValidationError('Add content in order to post.')
            
    class Meta:
        db_constraints = {
            'post_content_missing': 'CHECK (content IS NOT NULL)',
        }

    # check constraint that a post moderation note contains content
    def clean(self):
        super().clean()
        if self.moderated_note is None:
            raise ValidationError('Notes about moderations need to be included.')
            
    class Meta:
        db_constraints = {
            'post_moderation_content_missing': 'CHECK (moderated_note IS NOT NULL)',
        }

    # check constraint that a post id is set
    def clean(self):
        super().clean()
        if self.post_id is None:
            raise ValidationError('Post Id must be set.')
        
    class Meta:
        db_constraints = {
            'post_id_missing': 'CHECK (post_id IS NOT NULL)',
        }

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

    # check constraint that a reply contains content
    def clean(self):
        super().clean()
        if self.content is None:
            raise ValidationError('Add content in order to reply.')
            
    class Meta:
        db_constraints = {
            'reply_content_missing': 'CHECK (content IS NOT NULL)',
        }

    # check constraint that a reply moderation note contains content
    def clean(self):
        super().clean()
        if self.moderated_note is None:
            raise ValidationError('Notes about moderations need to be included.')
            
    class Meta:
        db_constraints = {
            'post_moderation_content_missing': 'CHECK (moderated_note IS NOT NULL)',
        }

    # check constraint that a reply id is set
    def clean(self):
        super().clean()
        if self.reply_id is None:
            raise ValidationError('Reply Id must be set.')
        
    class Meta:
        db_constraints = {
            'reply_id_missing': 'CHECK (reply_id IS NOT NULL)',
        }

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

    # check constraint that a building address is not empty
    def clean(self):
        super().clean()
        if self.address is None:
            raise ValidationError('Building address must be specified.')
            
    class Meta:
        db_constraints = {
            'building_address_missing': 'CHECK (address IS NOT NULL)',
        }

    # check constraint that building description is not empty
    def clean(self):
        super().clean()
        if self.description is None:
            raise ValidationError('Building description must be specifed.')
            
    class Meta:
        db_constraints = {
            'building_description_missing': 'CHECK (description IS NOT NULL)',
        }
    
class BuildingPost(models.Model):  # many to many linking table for when posts mention buildings
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)

    # check constraint that a building post id is set
    def clean(self):
        super().clean()
        if self.id is None:
            raise ValidationError('Id must be set.')
        
    class Meta:
        db_constraints = {
            'id_missing': 'CHECK (id IS NOT NULL)',
        }
    
class BuildingReply(models.Model): # many to many linking table for when replies mention buildings
    id = models.AutoField(primary_key=True)
    reply_id = models.ForeignKey(Reply, on_delete=models.CASCADE)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)

    # check constraint that a building reply id is set
    def clean(self):
        super().clean()
        if self.id is None:
            raise ValidationError('Id must be set.')
        
    class Meta:
        db_constraints = {
            'id_missing': 'CHECK (id IS NOT NULL)',
        }

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

    # check constraint that location description is not empty
    def clean(self):
        super().clean()
        if self.description is None:
            raise ValidationError('Location description must be specifed.')
            
    class Meta:
        db_constraints = {
            'location_description_missing': 'CHECK (description IS NOT NULL)',
        }

    # check constraint that a location id is set
    def clean(self):
        super().clean()
        if self.location_id is None:
            raise ValidationError('Location Id must be set.')
            
    class Meta:
        db_constraints = {
            'location_id_missing': 'CHECK (location_id IS NOT NULL)',
        }

class LocationPost(models.Model):  # many to many linking table for when posts mention locations
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    # check constraint that a location post id is set
    def clean(self):
        super().clean()
        if self.id is None:
            raise ValidationError('Id must be set.')
        
    class Meta:
        db_constraints = {
            'id_missing': 'CHECK (id IS NOT NULL)',
        }
    
class LocationReply(models.Model): # many to many linking table for when replies mention locations
    id = models.AutoField(primary_key=True)
    reply_id = models.ForeignKey(Reply, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    # check constraint that a location reply id is set
    def clean(self):
        super().clean()
        if self.id is None:
            raise ValidationError('Id must be set.')
        
    class Meta:
        db_constraints = {
            'id_missing': 'CHECK (id IS NOT NULL)',
        }