from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("nickname", "email", "is_pro")
    search_fields = ("nickname", "email")
    list_filter = ("is_pro",)
