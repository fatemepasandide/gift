from django.db import models

from .enums import PurchaseStatusEnum


class WishList(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    link = models.CharField(max_length=300)
    status = models.CharField(
        max_length=30,
        choices=PurchaseStatusEnum,
        default=PurchaseStatusEnum.NOT_PURCHASED
    )

