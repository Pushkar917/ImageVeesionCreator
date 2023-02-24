from django.db import models
from apps.common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _


class OriginalImage(TimeStampedUUIDModel):
    title = models.CharField(verbose_name=_("title"), max_length=24,  blank= False)
    image = models.ImageField(verbose_name=_("image"), blank=False)


    def __str__(self):
        return f"{self.title}'s image"

