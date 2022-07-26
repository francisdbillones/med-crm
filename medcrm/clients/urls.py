from django.shortcuts import redirect
from django.urls import path
from .views import ClientListView, client_detail

app_name = "clients"

urlpatterns = [
    path("", ClientListView.as_view(), name="clients_list"),
    path("<int:pk>", client_detail, name="client_detail"),
]
