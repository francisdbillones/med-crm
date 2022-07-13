from html.parser import HTMLParser
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.http import HttpRequest, HttpResponse

import django.contrib.auth as auth


def index(r: HttpRequest) -> HttpResponse:
    if not r.user.is_authenticated:
        return redirect("login")

    return HttpResponse(f"you're user {r.user}")


def login(r: HttpResponse) -> HTTPResponse:
    if r.method == "GET":
        return render(r, "login.html")

    elif r.method == "POST":
        username = r.POST["username"][0]
        password = r.POST["password"][0]
        user = auth.authenticate(r, username=username, password=password)

        if user is not None:
            login(r, user)
        else:
            return HttpResponse("hey! you're not who you say you are!")
