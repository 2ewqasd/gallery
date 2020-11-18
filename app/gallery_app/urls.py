from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from register import views as v
from upload.views import image_upload_view, image_show

urlpatterns = [
    path("", image_show, name="picture"),
    path("upload/", image_upload_view, name="upload"),
    path("admin/", admin.site.urls),
    path("register/", v.register, name="register"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('', include('django.contrib.auth.urls')),
]
