from rest_framework import serializers

from user.models import Profile
from wish_list.models import WishList
from rest_flex_fields import FlexFieldsModelSerializer


class WishListSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = WishList
        fields = (
            'user',
            'status',
            'link',
            'description',
            'name',
        )
        expandable_fields = {
            'user': (Profile, {'many': True})
        }

