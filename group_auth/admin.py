from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from .models import Users, CustomGroup
from import_export.admin import ExportActionMixin


class CustomUserAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('username', 'get_group')
    ordering = ['groups']

    # def group_name(self, obj):
    #     return "\n".join([p.users_set for p in obj.groups.filter()])
    # group_name.short_description = 'Group'


admin.site.register(Users, CustomUserAdmin)


class CustomGroupAdmin(ExportActionMixin, GroupAdmin):
    list_display = ('name', 'users_count', )
    fields = ['name', 'users']

    # def users_count(self, obj):
    #     pass
    # users_count.short_description = 'количество юзеров в группе'


admin.site.unregister(Group)
admin.site.register(CustomGroup, CustomGroupAdmin)