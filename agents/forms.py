from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Agent


class AgentModelForm(forms.ModelForm):
    model = Agent
    fields = ("email", "username", "first_name", "last_name")
