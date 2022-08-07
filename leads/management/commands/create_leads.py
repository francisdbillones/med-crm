from __future__ import annotations

import random
import os
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandParser
from leads.models import Lead, Category


def main(lead_count: int):
    with open("dummy_data/names.txt") as f:
        names = [name.strip() for name in f]

    with open("dummy_data/specialties.txt") as f:
        specialties = [specialty.strip() for specialty in f]

    pfps = os.listdir("dummy_data/pfps")

    for _ in range(lead_count):
        new_lead = dummy_lead(names, specialties, pfps)
        new_lead.save()


def dummy_lead(names: list[str], specialties: list[str], pfps: list[str]) -> Lead:
    unconverted = Category.objects.get(name="Unconverted")
    converted = Category.objects.get(name="Converted")

    first_name, last_name = random.sample(names, k=2)
    email = f"{first_name}{last_name}@gmail.com"
    category = random.choice((unconverted, converted))
    specialty = random.choice(specialties)
    phone = "".join(random.choices("0123456789", k=15))
    profile_picture = random.choice(pfps)

    date_added = random_date()
    converted_date = random_date(date_added)

    new_lead = Lead.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        category=category,
        specialty=specialty,
        phone=phone,
        profile_picture=profile_picture,
        date_added=date_added,
        converted_date=converted_date if category is converted else None,
    )

    return new_lead


def random_date(start: datetime = None) -> datetime:
    if start is None:
        start = datetime.now() - timedelta(days=365 * 5)
    end = datetime.now()

    date = start + timedelta(
        seconds=random.random() * (end.timestamp() - start.timestamp())
    )

    return date


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("leads", nargs=1, type=int)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        main(options["leads"][0])
