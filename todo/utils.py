from django.contrib.auth.forms import  (
    AuthenticationForm as DjangoAuthenticationForm, PasswordResetForm as DjangoPasswordResetForm,
    SetPasswordForm as DjangoSetPasswordForm
)
from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from .models import UsernameField


class AuthenticationForm(DjangoAuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"}))
    password = forms.CharField(
    label=_("Password"),
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
    )

class PasswordResetForm(DjangoPasswordResetForm):
    email = forms.EmailField(
    label=_("Email"),
    max_length=254,
    widget=forms.EmailInput(attrs={"autocomplete": "email", "class": "form-control"}),
    )

class SetPasswordForm(DjangoSetPasswordForm):
    new_password1 = forms.CharField(
    label=_("New password"),
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
    strip=False,
    help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
    )