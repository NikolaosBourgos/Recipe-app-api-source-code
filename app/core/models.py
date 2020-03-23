from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                                        PermissionsMixin
# Create your models here.


# This class provides the helper functions for creating a user or superuser
class UserManager (BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # password=none in case i want to create a user that is not active
        """Creates and Saves a New User"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # can't set the password above because it must be encrypted, so I will
        # call the set_password helper function
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and Saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create the Model. Extend from the AbstractBaseUser and the PermissionsMixin
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
