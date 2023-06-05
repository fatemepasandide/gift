from rest_framework import routers

from invite.views import InviteViewSet
from user.views import ProfileViewSet

router = routers.SimpleRouter()
router.register(r'', InviteViewSet, basename='invite')

urlpatterns = []

urlpatterns += router.urls
