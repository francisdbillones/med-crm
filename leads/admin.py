from django.contrib import admin

from .models import Lead, Category


admin.site.register(Category)
admin.site.register(Lead)
