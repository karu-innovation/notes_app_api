from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notes(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    