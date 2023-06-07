from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    phone_number=models.CharField(max_length=11,unique=True)
    full_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=['full_name',]
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin



