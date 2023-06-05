from rest_framework import viewsets

from invite.models import InvitationHistory
from invite.serializers import InviteSerializer


class InviteViewSet(viewsets.ModelViewSet):
    serializer_class = InviteSerializer
    queryset = InvitationHistory.objects.all()
