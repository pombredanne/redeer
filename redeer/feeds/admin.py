from django.contrib import admin

from redeer.feeds.models import Group, Feed, Item


class FeedAdmin(admin.ModelAdmin):
    list_display = ['title', 'group', 'last_updated']
    list_filter = ['group__user']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'feed', 'is_read', 'is_saved', 'created_on_time']
    list_filter = ['feed__group__user']
    search_fields = ['feed__title']


admin.site.register(Group)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Item, ItemAdmin)
