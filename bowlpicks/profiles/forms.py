from django import forms

from bowlpicks.profiles.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ('profile', )