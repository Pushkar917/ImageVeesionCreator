from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel

# Create your models here.

User = get_user_model()

class GlobalContactModel(TimeStampedUUIDModel):
    user = models.ForeignKey(User, related_name="user_contact_database", on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("name"), max_length=24,  blank=True)
    phone_number = models.CharField(verbose_name=_("phone_number"), max_length=18,  blank=True)
    is_spam = models.BooleanField(verbose_name=_("SPAM"), default=False, help_text=_("Is this a spam number?"))


    def __str__(self):
        return f"{self.user.username}'s contact in Global Directory"