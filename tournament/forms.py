from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Tournament, Stage


class NewTournament(ModelForm):
    class Meta:
        model = Tournament
        exclude = ['pk']
        widgets = {
            'players': CheckboxSelectMultiple(attrs={
                'style': 'list-style-type: none',
            }),
        }


class NewStage(ModelForm):
    class Meta:
        model = Stage
        fields = ['mode']
