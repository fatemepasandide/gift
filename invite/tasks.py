from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True)
def send_mail_task(self):
    send_mail(
        "Invitation Email",
        "You Invited",
        "support@example.com",
        ['fateme.psn@gmail.com'],
        fail_silently=False,
    )
    return "Done"
