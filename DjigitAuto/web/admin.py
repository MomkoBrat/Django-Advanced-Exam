from django.contrib import admin

from DjigitAuto.web.models import OfferComment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'creator_id', 'created_at']
    list_filter = ['creator_id', 'created_at']


admin.site.register(OfferComment, CommentAdmin)
