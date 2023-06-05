from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wish_list/', include('wish_list.urls')),
    path('user/', include('user.urls')),
]
