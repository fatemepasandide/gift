from rest_framework import routers

from wish_list.views import WishListViewSet

router = routers.SimpleRouter()
router.register(r'', WishListViewSet.as_view(), basename='wish-list')

urlpatterns = []

urlpatterns += router.urls
