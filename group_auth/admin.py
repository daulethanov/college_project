from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from .models import Users, CustomGroup
from import_export.admin import ExportActionMixin


class CustomUserAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('username', 'group_name')

    def group_name(self, obj):
        return obj.groups.name
    group_name.short_description = 'Group'


admin.site.register(Users, CustomUserAdmin)


class CustomGroupAdmin(ExportActionMixin, GroupAdmin):
    list_display = ('name', 'user_count')


    def user_count(self, obj):

        return obj.users_set.get().username
    user_count.short_description = 'количество юзеров в группе'


admin.site.unregister(Group)
admin.site.register(CustomGroup, CustomGroupAdmin)