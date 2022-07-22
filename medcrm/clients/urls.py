from django.shortcuts import redirect
from django.urls import path
from .views import clients_list, client_detail

app_name = "clients"

urlpatterns = [
    path("clients", clients_list, name="clients_list"),
    path("clients/<int:pk>/", client_detail, name="client_detail"),
]
