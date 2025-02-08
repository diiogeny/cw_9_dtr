from django.urls import path
from .views import RegisterView, CustomLoginView, CustomLogoutView, ProfileView, user_profile

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/<int:pk>/", user_profile, name="user_profile"),
]
