from django.db import models

from user.models import Profile
from .enums import PurchaseStatusEnum


class WishList(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    link = models.CharField(max_length=300)
    status = models.CharField(
        max_length=30,
        choices=PurchaseStatusEnum.choices,
        default=PurchaseStatusEnum.NOT_PURCHASED
    )

    def __str__(self):
        return f'{self.user} has {self.name}.'
