from django.urls import path
from . import views

urlpatterns = [
    path("", views.games_list, name="list"),
    path("create/", views.create_game, name="create"),
    path("<int:pk>/details/", views.game_details, name="details"),
    path("<int:pk>/edit/", views.edit_game, name="edit"),
    path("<int:pk>/delete/", views.delete_game, name="delete"),
]
