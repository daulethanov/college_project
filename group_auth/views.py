import random
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from .forms import *


def home(request):
    return render(request, 'index.html')


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            groups = Group.objects.all()
            group = random.choice(groups)
            if group.users_set.count() <= 10:
                group.users_set.add(user)
                group.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'account/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class GroupsList(ListView):
    model = Group
    template_name = 'index.html'
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super(GroupsList, self).get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


def view_groups(request):
    groups = Group.objects.all()
    users_by_group = {group: group.users_set.all() for group in groups}
    return render(request, 'groups.html', {'groups': groups, 'users_by_group': users_by_group})


class GroupDetail(DetailView):
    model = Group
    context_object_name = 'group_detail'
    template_name = 'index.html'