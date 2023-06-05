from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    email = models.EmailField(max_length=70, blank=True, unique=True)

    def __str__(self):
        return str(self.email)
