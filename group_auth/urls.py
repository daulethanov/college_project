from django.urls import path
from .views import *

urlpatterns = [
    path('', registration_view, name='home'),

    # path('register', registration_view, name='register'),
    # path('login', LoginUser.as_view(), name='login'),
    # path('logout', logout_user, name='logout'),

    path('group', view_groups, name='group'),

]
