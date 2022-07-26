from django.conf import settings
from django.db.models import QuerySet, Model
from django.http import HttpRequest
from .models import Client, ClientPlan


def navbar_clients(r: HttpRequest):
    client_ids = ClientPlan.objects.filter(representative=r.user.id).values("client")
    clients = Client.objects.filter(id__in=client_ids)
    if clients.count() > settings.N_CLIENTS_TO_SHOW_IN_NAVBAR:
        clients_to_show_in_navbar = clients[: settings.N_CLIENTS_TO_SHOW_IN_NAVBAR]
        more_clients = clients[settings.N_CLIENTS_TO_SHOW_IN_NAVBAR :][
            : settings.N_CLIENTS_TO_SHOW_IN_DROPDOWN
        ]

    else:
        clients_to_show_in_navbar = clients
        more_clients = Client.objects.none()

    return clients_to_show_in_navbar, more_clients
