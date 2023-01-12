from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'group_name')

    def group_name(self, obj):
        return obj.groups.name
    group_name.short_description = 'Group'


admin.site.register(Users, CustomUserAdmin)