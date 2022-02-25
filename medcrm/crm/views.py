from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.core.handlers.asgi import ASGIRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView

# Create your views here.
class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard.html"


class LoginView(DjangoLoginView):
    template_name = "login.html"
