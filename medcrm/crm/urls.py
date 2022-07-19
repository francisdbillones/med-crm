from django.shortcuts import redirect
from django.urls import path

from .views import dashboard, auth

urlpatterns = [
    path("", dashboard.index, name="dashboard"),
    path("dashboard", dashboard.dashboard, name="dashboard"),
    path("dashboard/clients", dashboard.view_clients, name="clients"),
    path("login", auth.login, name="login"),
    path("logout", auth.logout, name="logout"),
]
