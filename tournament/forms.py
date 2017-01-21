from django.forms import Form, ModelForm, CheckboxSelectMultiple, CharField
from .models import Tournament, Stage


class NewPlayer(Form):
    first_name = CharField(max_length=30, label='First name')
    last_name = CharField(max_length=30, label='Last name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


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
