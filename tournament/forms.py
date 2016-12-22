from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Tournament, Player, Stage


class NewPlayer(ModelForm):
    class Meta:
        model = Player
        exclude = ['pk']


class NewTournament(ModelForm):
    class Meta:
        model = Tournament
        exclude = ['pk']
        widgets = {
            'players': CheckboxSelectMultiple(attrs={
                'style': 'list-style-type: none; margin: 0; padding: 0; vertical-align: center;',
            }),
        }


class NewStage(ModelForm):
    class Meta:
        model = Stage
        fields = ['mode']
