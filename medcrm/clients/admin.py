from django.contrib import admin

from .models import Program, Client, Schedule, ClientPlan

admin.site.register(Program)
admin.site.register(Client)
admin.site.register(Schedule)
admin.site.register(ClientPlan)
