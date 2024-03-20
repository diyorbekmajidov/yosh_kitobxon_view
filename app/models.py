from django.db import models
from django.utils import timezone
from datetime import timedelta

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
    phonenumber = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname
    

class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key using chat_id
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(null=True, auto_now=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.fullname
    
    def save(self, *args, **kwargs):
        # Set the date_created if it's None
        if not self.date_created:
            self.date_created = timezone.now()

        # Set the end_date one month from the date_created
        if not self.end_date:
            self.end_date = self.date_created + timedelta(days=30)

        super().save(*args, **kwargs)
    
    
    
    
