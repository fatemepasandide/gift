from celery import shared_task


@shared_task(bind=True)
def send_mail(self):
    print("test")
    return "Done"
