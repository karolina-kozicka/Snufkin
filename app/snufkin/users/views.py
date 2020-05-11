from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
import django_registration

from .forms import RegisterForm
from .models import User


class HomeView(views.TemplateView):
    template_name = "home.html"


class LoginView(views.LoginView):
    template_name = "users/login.html"


class LogoutView(views.LogoutView):
    template_name = "users/logout.html"


class PasswordResetView(views.PasswordResetView):
    template_name = "users/password_reset.html"
    success_url = reverse_lazy("users:password_reset_done")
    email_template_name = "users/reset_emial.html"
    subject_template_name = "users/password_reset_subject.txt"


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "users/password_reset_done.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"


class PasswordChangeView(LoginRequiredMixin, views.PasswordChangeView):
    template_name = "users/password_change.html"
    success_url = reverse_lazy("users:password_change_done")


class PasswordChangeDoneView(LoginRequiredMixin, views.PasswordChangeDoneView):
    template_name = "users/password_change_done.html"


class RegistrationView(django_registration.backends.activation.views.RegistrationView):
    template_name = "registration/registration_form.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:registration_complete")
    disallowed_url = reverse_lazy("users:registration_disallowed")
    email_body_template = "registration/activation_email_body.txt"
    email_subject_template = "registration/activation_email_subject.txt"


class ActivationView(django_registration.backends.activation.views.ActivationView):
    template_name = "registration/activation_failed.html"
    success_url = reverse_lazy("users:registration_activation_complete")


class EditView(LoginRequiredMixin, generic.UpdateView):
    template_name = "users/edit_name.html"
    model = User
    fields = ("name",)
    success_url = reverse_lazy("users:edit")

    def get_object(self, queryset=None):
        return self.request.user
