from .models import Player

def get_single_player():
    return Player.objects.first()
