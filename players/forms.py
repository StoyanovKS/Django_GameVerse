from django import forms
from .models import Player

class PlayerCreateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("nickname", "email", "is_pro")
        widgets = {
            "nickname": forms.TextInput(attrs={"placeholder": "Enter your nickname..."}),
            "email": forms.TextInput(attrs={"placeholder": "Enter a valid email..."}),
        }

class PlayerEditForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("nickname", "achievements", "is_pro")
        widgets = {
            "nickname": forms.TextInput(attrs={"placeholder": "Enter your nickname..."}),
        }
