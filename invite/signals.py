from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import InvitationHistory
from .tasks import send_mail


@receiver(post_save, sender=InvitationHistory)
def my_handler(sender, **kwargs):
    send_mail()
    return None
