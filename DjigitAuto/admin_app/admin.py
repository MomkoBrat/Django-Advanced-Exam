from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission, Group

from DjigitAuto.accounts.models import DjigitAutoUser
from DjigitAuto.admin_app.forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'date_joined',
                    'is_active', 'is_staff', 'is_superuser')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email")
    ordering = ("email",)


admin.site.register(DjigitAutoUser, CustomUserAdmin)

staff_group, created = Group.objects.get_or_create(name='staff_group')
superuser_group, created = Group.objects.get_or_create(name='superuser_group')

staff_permissions = Permission.objects.filter(codename__in=['profile details', 'edit profile', 'delete profile',
                                                            'create offer', 'user offers', 'edit offer', 'delete offer',
                                                            'create comment', 'edit comment', 'delete comment'])
superuser_permissions = Permission.objects.all()

staff_group.permissions.set(staff_permissions)
superuser_group.permissions.set(superuser_permissions)