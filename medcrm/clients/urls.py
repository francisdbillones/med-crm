from django.shortcuts import redirect
from django.urls import path
from .views import ClientCreateView, ClientEditView, ClientListView, ClientDetailView

app_name = "clients"

urlpatterns = [
    path("", ClientListView.as_view(), name="client_list"),
    path("create", ClientCreateView.as_view(), name="client_create"),
    path("<int:pk>", ClientDetailView.as_view(), name="client_detail"),
    path("<int:pk>/edit", ClientEditView.as_view(), name="client_edit"),
]
