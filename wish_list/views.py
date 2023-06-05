from rest_framework import mixins, viewsets

from wish_list.models import WishList
from wish_list.serializers import WishListSerializer


class WishListViewSet(viewsets.ModelViewSet):
    serializer_class = WishListSerializer
    queryset = WishList.objects.all()
