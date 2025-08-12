from django.shortcuts import render, redirect, get_object_or_404
from players.utils import get_single_player
from .models import Game
from .forms import GameCreateForm, GameEditForm

def require_profile():
    # small helper to use in views
    player = get_single_player()
    if not player:
        return None, redirect("players:create")
    return player, None

def games_list(request):
    qs = Game.objects.all()  # Meta.ordering handles (-level, title)
    return render(request, "games.html", {"games": qs})

def create_game(request):
    player, redirect_resp = require_profile()
    if redirect_resp:
        return redirect_resp
    form = GameCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        game = form.save(commit=False)
        game.player = player
        game.save()
        return redirect("games:list")
    return render(request, "create-game.html", {"form": form})

def game_details(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, "details-game.html", {"game": game})

def edit_game(request, pk):
    player, redirect_resp = require_profile()
    if redirect_resp:
        return redirect_resp
    game = get_object_or_404(Game, pk=pk)
    form = GameEditForm(request.POST or None, instance=game)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("games:details", pk=game.pk)
    return render(request, "edit-game.html", {"form": form, "game": game})

def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        game.delete()
        return redirect("games:list")
    return render(request, "delete-game.html", {"game": game})
