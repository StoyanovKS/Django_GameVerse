from players.models import Player

def player_presence(request):
    return {"has_profile": Player.objects.exists()}
