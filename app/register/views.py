from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import Group


# Create your views here.


def register(response):
    """Registration for user witch add him in Unknown group"""
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            Unknown = Group.objects.get_or_create(name='Unknown')
            user.groups.add(Unknown)
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
