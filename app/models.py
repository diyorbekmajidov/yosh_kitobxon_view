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
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname
    

class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key using chat_id
    status = models.BooleanField(default=False)
    img   = models.ImageField(upload_to='payment/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.user.fullname
    
    
    
    
