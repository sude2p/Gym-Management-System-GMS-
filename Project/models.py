from django.db import models
from django.utils import timezone


# Create your models here.
class Member(models.Model):
    SEX_CHOICES= [('MALE','MALE'),('FEMALE','FEMALE'),('OTHER','OTHER')]
    PACKAGE_CHOICES = [('1 MONTH','1 MONTH'),('3 MONTHS','3 MONTHS'),('6 MONTHS','6 MONTHS'),('12 MONTHS','12 MONTHS')]
    PAYMENT_STATUS = [('PAID','PAID'),('DUE','DUE')]
    f_name = models.CharField(max_length=100, blank=False, null=False)
    l_name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=200, blank=True, null=True)
    mobile_number = models.IntegerField(blank=False,null=False,default='+977')
    email = models.EmailField(blank=True, unique=True,null=True)
    age = models.IntegerField(blank=False, null=False,default=18)
    sex = models.CharField(max_length=30, choices=SEX_CHOICES, null=False)
    package_selected = models.CharField(max_length=30, choices=PACKAGE_CHOICES, null=False)
    payment = models.CharField(max_length=30, choices=PAYMENT_STATUS, null=False)
    health_conditions = models.TextField()
    date_joined = models.DateField(blank=False, default=timezone.now ,null= False)
    date_finish = models.DateField(blank=False, default=timezone.now, null=False)
    profile_pic = models.ImageField(null=True, blank=True, default='user-default.png')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.f_name
    
    
