from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    SUPER_ADMIN = 1
    ADMIN = 2
    ROLE_CHOICES = (
      (ADMIN,'admin'),
      (SUPER_ADMIN,'super_admin')
    )
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=ADMIN)

class Contact(models.Model):
  FirstName = models.CharField(max_length=264,blank=False)
  LastName = models.CharField(max_length=264,blank=False)
  PhoneNo = models.CharField(max_length=264,blank=False)
  Email = models.EmailField(max_length=264,blank=False)
  Message = models.CharField(max_length=500,blank=False)

class Career(models.Model):  
  Name = models.CharField(max_length=264,blank=False)
  Email = models.EmailField(max_length=264,blank=False)
  PhoneNo = models.CharField(max_length=264,blank=False)
  Resume =  models.FileField(upload_to='documents/')
  Message = models.CharField(max_length=500,blank=False)

class Quotation(models.Model):  
  Name = models.CharField(max_length=264,blank=False)
  Email = models.EmailField(max_length=264,blank=False)
  PhoneNo = models.CharField(max_length=264,blank=False)
  BusinessSector = models.CharField(max_length=500,blank=False) 
  Message = models.CharField(max_length=500,blank=False)  


