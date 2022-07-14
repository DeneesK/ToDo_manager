from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm, UsernameField as DjangoUsernameField
from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UsernameField(DjangoUsernameField):
    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            "autocapitalize": "none",
            "autocomplete": "username",
            "class": "form-control",
        }


class UserCreationForm(DjangoUserCreationForm):
    email = forms.EmailField(
    label=_("Email"),
    max_length=254,
    widget=forms.EmailInput(attrs={"autocomplete": "email", "class": "form-control", "placeholder": "example@mail.com"}),
    )
    password1 = forms.CharField(
    label=_("Password"),
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
    help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
    label=_("Password confirmation"),
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
    strip=False,
    help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {"username": UsernameField}