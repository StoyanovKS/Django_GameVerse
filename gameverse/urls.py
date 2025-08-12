from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("core.urls", "core"), namespace="core")),
    path("player/", include(("players.urls", "players"), namespace="players")),
    path("games/", include(("games.urls", "games"), namespace="games")),
]
