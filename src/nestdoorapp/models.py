from django.db import models

# Create your models here.
<<<<<<< HEAD


=======
>>>>>>> 8522b437b9fae47a43db1fd1129628da3915022d
class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=255)

    def __str__(self):
<<<<<<< HEAD
        return f"{self.name} {self.detail}"
=======
        return f"{self.name} {self.detail}"
>>>>>>> 8522b437b9fae47a43db1fd1129628da3915022d
