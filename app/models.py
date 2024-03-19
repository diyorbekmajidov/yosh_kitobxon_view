from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=255)
    chat_id  = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    profession = models.CharField(max_length=255)
    agecategory = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    village = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
    
