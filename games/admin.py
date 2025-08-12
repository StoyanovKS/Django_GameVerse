from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "platform", "level", "player")
    list_filter = ("platform", "level")
    search_fields = ("title",)
