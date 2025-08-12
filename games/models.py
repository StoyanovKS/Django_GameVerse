from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from players.models import Player

class Game(models.Model):
    PC = "PC Games"
    CONSOLE = "Console Games"
    OTHER = "Other Games"
    PLATFORM_CHOICES = [(PC, PC), (CONSOLE, CONSOLE), (OTHER, OTHER)]

    title = models.CharField(max_length=130, validators=[MinLengthValidator(3)])
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default=OTHER)
    release_date = models.DateField()
    level = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    screenshot_url = models.URLField(blank=True)
    # delete all games when player is deleted (as required)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="games", editable=False)

    class Meta:
        ordering = ["-level", "title"]

    def __str__(self):
        return self.title
