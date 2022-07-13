from http.client import HTTPResponse
from django.shortcuts import render
from django.views import generic
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView

def index(r: HttpRequest) -> HttpResponse:
    return "hello"

def login(r: HttpResponse) -> HTTPResponse:
    return "login"