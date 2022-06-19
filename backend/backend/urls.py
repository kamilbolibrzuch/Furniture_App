from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/furniture_app/', include('djoser.urls')),
    path('api/furniture_app/', include('djoser.urls.authtoken')),
]
