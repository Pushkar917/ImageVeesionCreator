from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _  
from django.utils import timezone
from apps.users.managers import CustomUserManager
from django.core.validators import RegexValidator
import uuid



# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    username = models.CharField(verbose_name=_('Username'), max_length=255, unique=True)
    email = models.EmailField(verbose_name=_('Email Address'), unique=False)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50, unique=False)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50, unique=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    contact_list = models.JSONField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]


    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    @property

    def get_short_name(self):
        return self.username
    

