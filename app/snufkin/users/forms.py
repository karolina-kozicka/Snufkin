from django.forms import ModelForm
from django_registration.forms import RegistrationForm

from .models import User


class RegisterForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
        fields = [
            User.USERNAME_FIELD,
            "name",
            "password1",
            "password2",
        ]
