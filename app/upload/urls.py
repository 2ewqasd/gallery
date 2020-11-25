from django.urls import path
from upload.views import Image_upload, ShowPicture


urlpatterns = [
    path("", ShowPicture.as_view(), name="main"),
    path("upload/", Image_upload.as_view(), name="upload"),
]
