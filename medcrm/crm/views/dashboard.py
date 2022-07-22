from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

import django.contrib.auth as auth
import django.contrib.messages as messages
from django.conf import settings

from ..forms import LoginForm
from ..helpers import login_required
from ..models import Representative, Client, ClientPlan, Program, Schedule


@login_required
def index(r: HttpRequest) -> HttpResponse:
    return redirect("dashboard")


@login_required
def dashboard(r: HttpRequest) -> HttpResponse:
    client_ids = ClientPlan.objects.filter(representative__id=r.user.id).values(
        "client"
    )
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

    return render(r, "dashboard.html", context=context)


@login_required
def view_clients(r: HttpRequest) -> HttpResponse:
    client_plans = ClientPlan.objects.filter(representative=r.user.id)
    client_ids = client_plans.values("client")
    clients = Client.objects.filter(id__in=client_ids)

    context = {"clients": clients}

    return render(r, "dashboard.html", context=context)
