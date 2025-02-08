from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, RegisterForm
from ads.models import Ad

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("ad-list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("ad-list")

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("ad-list")

class ProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "accounts/profile.html"

    def get_object(self):
        return self.request.user

def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    ads = Ad.objects.filter(author=user, status="published")
    return render(request, "accounts/user_profile.html", {"profile_user": user, "ads": ads})
