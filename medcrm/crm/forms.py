import django.contrib.auth as auth
import django.forms as forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
