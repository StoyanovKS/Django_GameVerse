from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_player, name="create"),
    path("details/", views.player_details, name="details"),
    path("edit/", views.edit_player, name="edit"),
    path("delete/", views.delete_player, name="delete"),
]
