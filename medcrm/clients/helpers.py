from django.conf import settings
from django.db.models import QuerySet
from .models import Client


def navbar_clients(clients: QuerySet):
    if clients.count() > settings.N_CLIENTS_TO_SHOW_IN_NAVBAR:
        clients_to_show_in_navbar = clients[: settings.N_CLIENTS_TO_SHOW_IN_NAVBAR]
        more_clients = clients[settings.N_CLIENTS_TO_SHOW_IN_NAVBAR :][
            : settings.N_CLIENTS_TO_SHOW_IN_DROPDOWN
        ]

    else:
        clients_to_show_in_navbar = clients
        more_clients = Client.objects.none()

    return clients_to_show_in_navbar, more_clients
