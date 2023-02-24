from django.contrib import admin
from apps.versionImage.models import PortFolioImageVesions, LandscapeImageVesions, LogoImageVersions

# Register your models here.
admin.site.register(PortFolioImageVesions)
admin.site.register(LandscapeImageVesions)
admin.site.register(LogoImageVersions)

