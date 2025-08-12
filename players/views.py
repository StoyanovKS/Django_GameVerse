from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerCreateForm, PlayerEditForm
from .models import Player
from .utils import get_single_player

def create_player(request):
    if Player.objects.exists():
        return redirect("games:list")
    form = PlayerCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("games:list")
    return render(request, "create-player.html", {"form": form})

def player_details(request):
    player = get_object_or_404(Player, pk=get_single_player().pk) if get_single_player() else None
    if not player:
        return redirect("players:create")
    from games.models import Game
    games_qs = Game.objects.filter(player=player).order_by("-level", "title")[:3]
    return render(request, "details-player.html", {"player": player, "top_games": games_qs})

def edit_player(request):
    player = get_single_player()
    if not player:
        return redirect("players:create")
    form = PlayerEditForm(request.POST or None, instance=player)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("players:details")
    return render(request, "edit-player.html", {"form": form})

def delete_player(request):
    player = get_single_player()
    if not player:
        return redirect("core:index")
    if request.method == "POST":
        player.delete()  # cascades games
        return redirect("core:index")
    return render(request, "delete-player.html")
