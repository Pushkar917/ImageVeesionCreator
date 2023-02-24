from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel
from django.db import models
from apps.uploader.models import OriginalImage

# Create your models here.




class PortFolioImageVesions(models.Model):
    portfolio_field = models.ImageField(verbose_name=_("portfolio_photo"))
    original_image = models.OneToOneField(OriginalImage, related_name="portfolio_image", on_delete=models.CASCADE)

    def __str__(self):
        return f"portolio_resolution of {self.original_image.title}"
    
class LandscapeImageVesions(models.Model):
    landscape_field = models.ImageField(verbose_name=_("landscape_photo"))
    original_image = models.OneToOneField(OriginalImage, related_name="landscape_image", on_delete=models.CASCADE)

    def __str__(self):
        return f"landscape_resolution of {self.original_image.title}"
    
class LogoImageVersions(models.Model):
    logo_field = models.ImageField(verbose_name=_("logo_photo"))
    original_image = models.OneToOneField(OriginalImage, related_name="logo_image", on_delete=models.CASCADE)

    def __str__(self):
        return f"logo_resolution of {self.original_image.title}"

