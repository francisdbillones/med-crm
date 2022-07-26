from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from medcrm.helpers import LoginRequiredMixin, login_required
from .models import Representative, Client, ClientPlan, Program, Schedule
from .helpers import navbar_clients


class ClientListView(ListView, LoginRequiredMixin):
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


class ClientDetailView(DetailView, LoginRequiredMixin):
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
