from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Tournament


class NewTournament(ModelForm):
    class Meta:
        model = Tournament
        exclude = ['pk']
        widgets = {
            'players': CheckboxSelectMultiple(attrs={
                'style': 'list-style-type: none',
            }),
        }
