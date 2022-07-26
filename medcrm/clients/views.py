import django.forms as forms
from django.urls import reverse
import django.views.generic as generic
from django.http import HttpRequest, HttpResponse

from medcrm.helpers import LoginRequiredMixin
from .models import Representative, Client, ClientPlan, Program, Schedule
from .helpers import navbar_clients


class ClientListView(generic.ListView, LoginRequiredMixin):
    model = Client
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients_to_show_in_navbar, more_clients = navbar_clients(self.request)

        context.update(
            {
                "clients_to_show_in_navbar": clients_to_show_in_navbar,
                "more_clients": more_clients,
            }
        )

        return context


class ClientDetailView(generic.DetailView, LoginRequiredMixin):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients_to_show_in_navbar, more_clients = navbar_clients(self.request)

        context.update(
            {
                "clients_to_show_in_navbar": clients_to_show_in_navbar,
                "more_clients": more_clients,
            }
        )

        return context


class ClientCreateView(generic.CreateView, LoginRequiredMixin):
    model = Client
    fields = [
        "firstname",
        "lastname",
        "email",
        "phone",
        "specialty",
        "geolocation_url",
        "profile_picture",
    ]
    template_name = "clients/client_create.html"
