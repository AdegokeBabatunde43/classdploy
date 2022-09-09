from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    id_user=models.IntegerField()
    address = models.CharField(max_length=255, blank=True)
    state= models.CharField(max_length=255, blank=True)
    city=models.CharField(max_length=255, blank=True)
    reason=models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
    
