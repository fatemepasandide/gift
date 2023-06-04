from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    email = models.EmailField(max_length=70, blank=True, unique=True)
    # wish_list = models.ForeignKey(WishList)

    def __str__(self):
        return str(self.email)
