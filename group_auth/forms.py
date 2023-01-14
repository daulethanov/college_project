from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from group_auth.models import Users, STREET


class RegistrationForm(forms.Form):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone = forms.IntegerField(label='Номер телефона', widget=forms.NumberInput(attrs={'class': 'form-input', 'type': 'number', 'value': 7}))
    iin = forms.IntegerField(label='ИИН', widget=forms.NumberInput(attrs={'class': 'form-input', }))
    job_title = forms.CharField(label='Должность', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    city = forms.ChoiceField(label='Город, Район', choices=STREET, widget=forms.Select(attrs={'class': 'form-input'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = Users.objects.create_user(
            self.cleaned_data["username"],
            self.cleaned_data["password1"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            patronymic=self.cleaned_data["patronymic"],
            phone=self.cleaned_data["phone"],
            iin=self.cleaned_data["iin"],
            job_title=self.cleaned_data["job_title"],
            city=self.cleaned_data["city"],
        )
        return user


class LoginUserForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']