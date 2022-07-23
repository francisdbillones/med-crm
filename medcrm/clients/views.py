from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

import django.contrib.auth as auth
import django.contrib.messages as messages
from django.conf import settings

from medcrm.helpers import login_required
from .models import Representative, Client, ClientPlan, Program, Schedule
from .helpers import navbar_clients


@login_required
def clients_list(r: HttpRequest) -> HttpResponse:
    client_ids = ClientPlan.objects.filter(representative=r.user.id).values("client")
    clients = Client.objects.filter(id__in=client_ids)

    clients_to_show_in_navbar, more_clients = navbar_clients(clients)

    context = {
        "clients": clients,
        "clients_to_show_in_navbar": clients_to_show_in_navbar,
        "more_clients": more_clients,
    }

    return render(r, "clients_list.html", context=context)


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
