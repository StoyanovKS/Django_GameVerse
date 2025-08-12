from django import forms
from .models import Game

class GameCreateForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ("player",)
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter games title..."}),
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "level": forms.NumberInput(attrs={"min": 1, "max": 10}),
            "screenshot_url": forms.URLInput(attrs={"placeholder": "Enter screenshot URL..."}),
        }

class GameEditForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ("player",)
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "level": forms.NumberInput(attrs={"min": 1, "max": 10}),
        }
