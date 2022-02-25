from django.contrib import admin

from .models import Representative, Program, Client, Schedule, ClientPlan

registered = [Representative, Program, Client, Schedule, ClientPlan]

for r in registered:
    admin.site.register(r)
