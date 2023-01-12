from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from group_auth.models import Users


class RegistrationForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'patronymic', 'phone', 'city', 'job_title', 'iin', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']