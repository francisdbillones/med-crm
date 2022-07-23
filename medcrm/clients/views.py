from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

import django.contrib.auth as auth
import django.contrib.messages as messages
from django.conf import settings

from medcrm.helpers import login_required
from .models import Representative, Client, ClientPlan, Program, Schedule


@login_required
def clients_list(r: HttpRequest) -> HttpResponse:
    client_ids = ClientPlan.objects.filter(representative=r.user.id).values("client")
    clients = Client.objects.filter(id__in=client_ids)
    if clients.count() > settings.N_CLIENTS_TO_SHOW_IN_NAVBAR:
        clients_to_show_in_navbar = clients[: settings.N_CLIENTS_TO_SHOW_IN_NAVBAR]
        more_clients = clients[settings.N_CLIENTS_TO_SHOW_IN_NAVBAR :][
            : settings.N_CLIENTS_TO_SHOW_IN_DROPDOWN
        ]

        context = {
            "clients_to_show_in_navbar": clients_to_show_in_navbar,
            "more_clients": more_clients,
        }

    else:
        clients_to_show_in_navbar = clients

        context = {
            "clients_to_show_in_navbar": clients_to_show_in_navbar,
        }

    return render(r, "clients_list.html", context=context)


@login_required
def client_detail(r: HttpRequest, pk: int) -> HttpResponse:
    client = Client.objects.get(id=pk)

    context = {"client": client}

    return render(r, "client_detail.html", context=context)
