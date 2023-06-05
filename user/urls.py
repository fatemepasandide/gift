from rest_framework import routers

from user.views import ProfileViewSet

router = routers.SimpleRouter()
router.register(r'', ProfileViewSet, basename='profile')

urlpatterns = []

urlpatterns += router.urls
