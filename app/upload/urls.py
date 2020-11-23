from django.urls import path
from upload.views import image_upload_view, image_show


urlpatterns = [
    path("", image_show, name="picture"),
    path("upload/", image_upload_view, name="upload"),
]
