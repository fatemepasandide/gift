from django.db import models


class PurchaseStatusEnum(models.Model):
    PURCHASED = 'Purchased'
    NOT_PURCHASED = 'Not purchased'

