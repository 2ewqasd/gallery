from .forms import RegisterForm
from django.views.generic.edit import FormView


class RegisterView(FormView):
    """Registration form"""
    template_name = 'register/register.html'
    form_class = RegisterForm
