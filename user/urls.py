from rest_framework import routers

from user.views import ProfileViewSet

router = routers.SimpleRouter()
router.register(r'', ProfileViewSet.as_view(), basename='profile')

urlpatterns = []

urlpatterns += router.urls
