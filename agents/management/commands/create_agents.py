from __future__ import annotations

import random
import os
from datetime import datetime, timedelta
from django.utils import timezone

from django.core.management.base import BaseCommand, CommandParser
from agents.models import Agent


def main(agent_count: int):
    with open("dummy_data/names.txt") as f:
        names = [name.strip() for name in f]

    pfps = os.listdir("dummy_data/pfps")

    for _ in range(agent_count):
        new_agent = dummy_lead(names, pfps)
        new_agent.save()


def dummy_lead(names: list[str], pfps: list[str]) -> Agent:
    first_name, last_name = random.sample(names, k=2)
    email = f"{first_name}{last_name}@gmail.com"
    phone = "".join(random.choices("0123456789", k=15))
    profile_picture = random.choice(pfps)

    date_joined = random_date()

    new_agent = Agent.objects.create(
        username=f"{first_name}{last_name}{random.randint(1, 100)}",
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        profile_picture=profile_picture,
        date_joined=date_joined,
    )

    return new_agent


def random_date(start: datetime = None) -> datetime:
    if start is None:
        start = timezone.now() - timedelta(days=365 * 5)
    end = timezone.now()

    date = start + timedelta(
        seconds=random.random() * (end.timestamp() - start.timestamp())
    )

    return date


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("agents", nargs=1, type=int)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        main(options["agents"][0])
