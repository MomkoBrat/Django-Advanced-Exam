from django.contrib import admin

from DjigitAuto.accounts.models import DjigitAutoUser
from DjigitAuto.web.models import OfferComment


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(DjigitAutoUser, CustomUserAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'modified_at', 'car_offer', 'user')
    list_filter = ('created_at', 'modified_at', 'car_offer', 'user')
    search_fields = ('text',)
    date_hierarchy = 'created_at'


admin.site.register(OfferComment, CommentAdmin)
