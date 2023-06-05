from rest_framework import serializers

from invite.models import InvitationHistory
from user.models import Profile


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationHistory
        fields = (
            'invited',
            'inviter',
        )
