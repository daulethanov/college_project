from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from .models import Users, CustomGroup
from import_export.admin import ExportActionMixin


class CustomUserAdmin(ExportActionMixin, admin.ModelAdmin):
    ordering = ['groups']
    list_display = ('username', 'get_group')


admin.site.register(Users, CustomUserAdmin)


class CustomGroupAdmin(ExportActionMixin, GroupAdmin):
    list_display = ('name', 'users_count',)
    fields = ['name', 'users']


admin.site.unregister(Group)
admin.site.register(CustomGroup, CustomGroupAdmin)