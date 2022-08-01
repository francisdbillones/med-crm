from django.contrib import admin

from .models import Lead, LeadPlan, Category, Program, TargetProduct

admin.site.register(Lead)
admin.site.register(LeadPlan)
admin.site.register(Category)
admin.site.register(Program)
admin.site.register(TargetProduct)
