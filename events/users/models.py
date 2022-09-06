from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from eventlist.models import Event
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = False
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD + '__iexact': username})


class User(AbstractUser):
    
    username = None
    email = models.EmailField(
        max_length=255, unique=True, null=True)
    interested_events = models.ManyToManyField(
        Event, blank=True, related_name="interested_events", verbose_name="Interested Events")
    city = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["id", "email"]
        
    objects = UserManager()


