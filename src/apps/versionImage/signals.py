import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.uploader.models import OriginalImage
from apps.versionImage.models import PortFolioImageVesions, LandscapeImageVesions, LogoImageVersions
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Importing the StringIO module.
from io import StringIO,BytesIO



logger = logging.getLogger("__name__")

@receiver(post_save, sender=OriginalImage)
def create_oriimage_portfolio(sender, instance, created,**kwargs):
    if created:
        img_io = BytesIO()
        original_image = Image.open(instance.image.path)
        cropped_img = original_image.crop((0, 0, 1500, 1100))
        cropped_img.save(img_io, format='JPEG', quality=100)
        img_content = ContentFile(img_io.getvalue(), 'portfolio_'+ instance.title + '.jpg')
        PortFolioImageVesions.objects.create(portfolio_field=img_content,original_image=instance)


@receiver(post_save, sender=OriginalImage)
def save_image_portfolio(sender, instance, **kwargs):
 
    # here portfolio_image is related name for original image as foreign key
    instance.portfolio_image.save()
    logger.info("Portfolio image created")







@receiver(post_save, sender=OriginalImage)
def create_origimages_landscape(sender, instance, created,**kwargs):
    if created:
        img_io = BytesIO()
        original_image = Image.open(instance.image.path)
        cropped_img = original_image.crop((0, 0, 800, 1500))
        cropped_img.save(img_io, format='JPEG', quality=100)
        img_content = ContentFile(img_io.getvalue(), 'landscape_'+ instance.title + '.jpg')
        LandscapeImageVesions.objects.create(landscape_field=img_content,original_image=instance)


@receiver(post_save, sender=OriginalImage)
def save_image_landscape(sender, instance, **kwargs):
 
    # here portfolio_image is related name for original image as foreign key
    instance.landscape_image.save()
    logger.info("Landscape image created")



@receiver(post_save, sender=OriginalImage)
def create_origimages_logo(sender, instance, created,**kwargs):
    if created:
        img_io = BytesIO()
        original_image = Image.open(instance.image.path)
        cropped_img = original_image.crop((0, 0, 500, 500))
        cropped_img.save(img_io, format='JPEG', quality=100)
        img_content = ContentFile(img_io.getvalue(), 'logo_'+ instance.title + '.jpg')
        LogoImageVersions.objects.create(logo_field=img_content,original_image=instance)


@receiver(post_save, sender=OriginalImage)
def save_image_landscape(sender, instance, **kwargs):
 
    # here portfolio_image is related name for original image as foreign key
    instance.logo_image.save()
    logger.info("Landscape image created")








