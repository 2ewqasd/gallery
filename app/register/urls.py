from django.urls import path
from register.views import Register

urlpatterns = [
    path("register/", Register.as_view(), name="Register"),
]
