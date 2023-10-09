from django.db import models

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
        return f"{self.first_name} {self.last_name}"
