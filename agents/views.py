from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from .models import Agent
from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"
    model = Agent


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    context_object_name = "agent"
    model = Agent

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        form.save(commit=True)
        return super().form_valid(form)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    model = Agent


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    context_object_name = "agent"
    model = Agent

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"
    model = Agent

    def get_success_url(self):
        return reverse("agents:agent-list")
