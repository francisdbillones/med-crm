from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Representative, Program, Client, Schedule, ClientPlan

admin.site.register(Representative, UserAdmin)
admin.site.register(Program)
admin.site.register(Client)
admin.site.register(Schedule)
admin.site.register(ClientPlan)
