from django.views.generic.list import ListView
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
        clients_to_show_in_navbar, more_clients = navbar_clients(context["object_list"])

        context.update(
            {
                "clients_to_show_in_navbar": clients_to_show_in_navbar,
                "more_clients": more_clients,
            }
        )

        return context


@login_required
def client_detail(r: HttpRequest, pk: int) -> HttpResponse:
    client_ids = ClientPlan.objects.filter(representative=r.user.id).values("client")
    clients = Client.objects.filter(id__in=client_ids)

    client = Client.objects.get(id=pk)

    clients_to_show_in_navbar, more_clients = navbar_clients(clients)

    context = {
        "client": client,
        "clients_to_show_in_navbar": clients_to_show_in_navbar,
        "more_clients": more_clients,
    }

    return render(r, "client_detail.html", context=context)
