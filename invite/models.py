from django.db import models

from user.models import Profile


class InvitationHistory(models.Model):
    inviter = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True)
    invited = models.EmailField(max_length=30)

    def __str__(self):
        return str(self.inviter)
