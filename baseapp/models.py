from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone                                                                                           

# Create your models here.


# The Custom User

class CustomUserManager(BaseUserManager):
  def create_user(self, email, password= None, **extra_fields):
    if not email:
      raise ValueError("Users must provide an email address")
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using = self._db)
    return user
  
  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.is_default('is_staff', True)
    extra_fields.is_default('is_superuser', True)
    return self.create_user(email, password, **extra_fields)
  

class CustomUser(AbstractBaseUser, PermissionsMixin):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)

    
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = [
    'first_name', 'last_name'
  ]

  objects = CustomUserManager()

  def __str__(self):
    return self.email
