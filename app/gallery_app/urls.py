from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('', include('django.contrib.auth.urls')),
    path('', include('upload.urls')),
    path('', include('register.urls'))
]
