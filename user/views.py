from rest_framework import viewsets

from user.models import Profile
from user.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
