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



