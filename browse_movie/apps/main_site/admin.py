from django.contrib import admin

from .models import WatchList


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['user', 'movies_id']
