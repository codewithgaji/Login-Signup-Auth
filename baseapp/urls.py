from django.urls import path, include
from .views import signup_view, home
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path("", home, name="home"),
  path("signup/", signup_view, name="signup"),
  path("accounts/", include("django.contrib.auth.urls")),
  path("logout/", LogoutView.as_view(), name="logout")
]
