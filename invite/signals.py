from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import InvitationHistory
from .tasks import send_mail_task


@receiver(post_save, sender=InvitationHistory)
def my_handler(sender, **kwargs):
    send_mail_task()
    return None
