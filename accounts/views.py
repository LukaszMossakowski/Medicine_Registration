from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from accounts.forms import UserCreation, EditProfileForm


class CreateUserView(CreateView):
    model = User
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = "manage_specialisation.html"


class MyProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "my_profile.html", {"user":request.user})


class EditProfileView(View):
    def get(self, request):
        form=EditProfileForm(instance=request.user)
        return render(request, "edit_profile.html", {"form":form})

    def post(self,request):
        form=EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("my_profile")
        return render(request, "edit_profile.html", {"form":form})