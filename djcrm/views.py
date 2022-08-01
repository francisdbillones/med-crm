from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class LoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request, "Login successful.")
        return super().form_valid(form)


class LogoutView(LogoutView):
    def form_valid(self, form):
        messages.success(self.request, "Logout successful.")
        return super().form_valid(form)
