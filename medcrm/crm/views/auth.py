from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

import django.contrib.auth as auth
import django.contrib.messages as messages
from django.conf import settings

from ..forms import LoginForm
from ..helpers import login_required
from ..models import Representative, Client, ClientPlan, Program, Schedule


def login(r: HttpRequest) -> HTTPResponse:
    form = LoginForm(r.POST or None)

    if r.POST and form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(r, user)
            messages.success(r, "Login successful.")
            return redirect("/") # redirect to index

        else:
            messages.error(
                r, "Invalid login. Check your username and password and try again."
            )

    return render(r, "login.html", {"form": form})


@login_required
def logout(r: HttpRequest) -> HttpResponse:
    auth.logout(r)
