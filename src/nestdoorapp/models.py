from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.

class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name} {self.detail}"
    
class UserExt(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    about_me = models.TextField()
        
      
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
    title = models.CharField(max_length=255)
    datetime_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="posts")
    content = models.TextField()
    number_replies = models.IntegerField(default=0)
    # datetime_last_edited = models.DateTimeField(null=True)
    
    #Moderation functionality removed for the time being.
    # moderation
    # datetime_last_moderated = models.DateTimeField(null=True)
    # last_moderated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="posts_moderated")
    # moderated_note = models.TextField()
    
    def clean(self):
        super().clean()
        # check constraint that a post contains content
        if self.content is None:
            raise ValidationError('Add content in order to post.')
        if self.title is None:
            raise ValidationError('Add title in order to post.')
        # check constraint that a post moderation note contains content
        #if self.moderated_note is None:
            #raise ValidationError('Notes about moderations need to be included.')
        # check constraint that a post id is set
        #if self.post_id is None:
        #   raise ValidationError('Post Id must be set.')
            
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(content__isnull=False), name="post_content_missing"),
            #'post_content_missing': 'CHECK (content IS NOT NULL)',
            #models.CheckConstraint(check=models.Q(moderated_note__isnull=False), name="post_moderation_content_missing"),
            #'post_moderation_content_missing': 'CHECK (moderated_note IS NOT NULL)',
            #models.CheckConstraint(check=models.Q(post_id__isnull=False), name="post_id_missing")
            #'post_id_missing': 'CHECK (post_id IS NOT NULL)',
        ]
        

class Reply(models.Model):
    # main
    reply_id = models.AutoField(primary_key=True)
    for_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    #For now all replies are directly to the main post... need to reapproach replying to replies.
    #for_reply_id = models.ForeignKey('self', on_delete=models.CASCADE)
    datetime_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="replies")
    content = models.TextField()
    #datetime_last_edited = models.DateTimeField(null=True)
    
    # moderation
    # datetime_last_moderated = models.DateTimeField(null=True)
    # last_moderated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="replies_last_moderated")
    # moderated_note = models.TextField()
    
    def clean(self):
        super().clean()
        # check constraint that a reply contains content
        if self.content is None:
            raise ValidationError('Add content in order to reply.')
        # check constraint that a reply id is set
        # if self.reply_id is None:
        #     raise ValidationError('Reply Id must be set.')
        # check constraint that a reply moderation note contains content
        # if self.moderated_note is None:
        #     raise ValidationError('Notes about moderations need to be included.')
            
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(content__isnull=False), name="reply_content_missing"),
            #'reply_content_missing': 'CHECK (content IS NOT NULL)',
            # models.CheckConstraint(check=models.Q(moderated_note__isnull=False), name="reply_moderation_content_missing"),
            #'post_moderation_content_missing': 'CHECK (moderated_note IS NOT NULL)',
            models.CheckConstraint(check=models.Q(reply_id__isnull=False), name="reply_id_missing")
            #'reply_id_missing': 'CHECK (reply_id IS NOT NULL)',
        ]

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
    
    def clean(self):
        super().clean()
        # check constraint that a building address is not empty
        if self.address is None:
            raise ValidationError('Building address must be specified.')
        # check constraint that building description is not empty
        if self.description is None:
            raise ValidationError('Building description must be specifed.')
            
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(address__isnull=False), name="building_address_missing"),
            #'building_address_missing': 'CHECK (address IS NOT NULL)',
            models.CheckConstraint(check=models.Q(description__isnull=False), name="building_description_missing")
            #'building_description_missing': 'CHECK (description IS NOT NULL)'
        ]
        
    
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
        constraints = [
            models.CheckConstraint(check=models.Q(id__isnull=False), name="buildingpost_id_missing")
            #'id_missing': 'CHECK (id IS NOT NULL)',
        ]
    
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
        constraints = [
            models.CheckConstraint(check=models.Q(id__isnull=False), name="buildingreply_id_missing")
            #'id_missing': 'CHECK (id IS NOT NULL)',
        ]

class Location(models.Model): # locations within buildings
    location_id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(Building, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    datetime_added = models.DateTimeField()
    number_mentions = models.IntegerField()
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    description = models.TextField()
    
    def clean(self):
        super().clean()
        # check constraint that either the building or the longitude and latitude must be set
        if self.building_id is None and (self.gps_longitude is None or self.gps_latitude is None):
            raise ValidationError('Either the building or gps coordinates must be specified.')
        # check constraint that location description is not empty
        if self.description is None:
            raise ValidationError('Location description must be specifed.')
        # check constraint that a location id is set
        if self.location_id is None:
            raise ValidationError('Location Id must be set.')
        
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(building_id__isnull=False) | \
                (models.Q(gps_longitude__isnull=False) & (models.Q(gps_latitude__isnull=False))), \
                name="location_building_or_gps_coords"),
            #'location_building_or_gps_coords': 'CHECK (building_id IS NOT NULL OR (gps_longitude IS NOT NULL AND gps_latitude IS NOT NULL))',
            models.CheckConstraint(check=models.Q(description__isnull=False), name="location_description_missing"),
            #'location_description_missing': 'CHECK (description IS NOT NULL)',
            models.CheckConstraint(check=models.Q(location_id__isnull=False), name="location_id_missing")
            #'location_id_missing': 'CHECK (location_id IS NOT NULL)',
        ]


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
        constraints = [
            models.CheckConstraint(check=models.Q(id__isnull=False), name="locationpost_id_missing")
            #'id_missing': 'CHECK (id IS NOT NULL)',
        ]
    
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
        constraints = [
            models.CheckConstraint(check=models.Q(id__isnull=False), name="locationreply_id_missing")
            #'id_missing': 'CHECK (id IS NOT NULL)',
        ]