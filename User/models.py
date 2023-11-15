from django.db import models
from Project.models import Member
from django.utils import timezone



# Create your models here.



class Profile(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, blank= False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True,null=True)
    sex = models.CharField(max_length=100, default='MALE')
    phone = models.IntegerField(blank=True,null=True)
    picture =  models.ImageField(null=True, blank=True, default='user-default.png')
    initial_biceps_size = models.IntegerField(blank=True,null=True)
    initial_chest_size = models.IntegerField(blank=True,null=True)
    initial_heart_rate = models.IntegerField(blank=True,null=True)
    initial_thigh_size = models.IntegerField(blank=True,null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
 


