from django.db import models
from django.utils.translation import gettext_lazy as _


class PurchaseStatusEnum(models.TextChoices):
    PURCHASED = 'PR', _('Purchased')
    NOT_PURCHASED = 'NOT', _('Not purchased')
