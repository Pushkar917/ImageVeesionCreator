from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.globalContactData.models import GlobalContactModel
from django.contrib.auth import get_user_model
import logging


User = get_user_model()

logger = logging.getLogger("__name__")

@receiver(post_save, sender=User)
def create_contact_database(sender, instance, created,**kwargs):
    if created:
        if instance.contact_list:
            contact_data = list(instance.contact_list.items())
            for i in range(0,len(contact_data)):
                GlobalContactModel.objects.create(user_id=instance.pkid,name=contact_data[i][0], phone_number=contact_data[i][1])
               



        


        
@receiver(post_save, sender=User)
def save_contact_database(sender, instance, **kwargs):
    if instance.phone_number:
        type(instance).objects.filter(pk=instance.pk).update(phone_number = instance.phone_number)
    return