from upload.models import Picture
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class Image_upload(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """A view that displays a upload's form"""

    permission_required = 'upload.add_picture'
    login_url = '/login/'
    model = Picture
    fields = ['title', 'image']
    success_url = '/'


class ShowPicture(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """A page representing a list of objects."""

    permission_required = 'upload.view_picture'
    login_url = '/login/'
    model = Picture
    paginate_by = 9

    def get_context_data(self, **kwargs):
        """ Take objects and show them"""
        context = super().get_context_data(**kwargs)
        return context
