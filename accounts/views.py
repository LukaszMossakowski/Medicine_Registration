from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserCreation


class CreateUserView(CreateView):
    model = User
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = "manage_specialisation.html"