from django.db import models
from django.contrib.auth.models import AbstractBaseUser,    BaseUserManager, PermissionsMixin
from .managers import UserManager
# Create your models here.

class customUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name=models.CharField(max_length=254, null=True, blank=True)
    last_name=models.CharField(max_length=254, null=True, blank=True)
    photo=models.ImageField(upload_to='profilePics/',null=True,blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)