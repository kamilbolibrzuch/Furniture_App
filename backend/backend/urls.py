from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/furniture_app/', include('djoser.urls')),
    path('api/furniture_app/', include('djoser.urls.authtoken')),
    path('api/furniture_app/', include('post.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
