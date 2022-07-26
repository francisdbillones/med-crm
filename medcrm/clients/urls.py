from django.shortcuts import redirect
from django.urls import path
from .views import ClientCreateView, ClientListView, ClientDetailView

app_name = "clients"

urlpatterns = [
    path("", ClientListView.as_view(), name="client_list"),
    path("<int:pk>", ClientDetailView.as_view(), name="client_detail"),
    path("<int:pk>/create", ClientCreateView.as_view(), name="client_create")
]
