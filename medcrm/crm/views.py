from html.parser import HTMLParser
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.http import HttpRequest, HttpResponse

import django.contrib.auth as auth
import django.contrib.messages as messages

from .forms import LoginForm


def index(r: HttpRequest) -> HttpResponse:
    if not r.user.is_authenticated:
        return redirect("login")

    return render(r, "dashboard.html")


def login(r: HttpRequest) -> HTTPResponse:
    form = LoginForm(r.POST or None)

    if r.POST and form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(r, user)
            messages.success(r, "Login successful.")
            return redirect("index")

        else:
            messages.error(
                "Invalid login. Check your username and password and try again."
            )

    return render(r, "login.html", {"form": form})


def logout(r: HttpRequest) -> HttpResponse:
    if r.user.is_authenticated:
        auth.logout(r)
        messages.success(r, "Logout successful.")
    else:
        messages.error(r, "You're not logged in.")

    return redirect("login")
