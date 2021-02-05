from django.views.generic.edit import CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy


class Register(CreateView):
    """
    Registration form
    """
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'loader.html'
