from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Tournament, Stage, Player
from .forms import NewTournament


def main(request):
    tournaments = Tournament.objects.all()
    context = {
        'tournaments': tournaments,
    }
    is_tourn_admin = request.user.groups.filter(name='tournament_admin')
    if is_tourn_admin:
        tournament_form = NewTournament()
        context['new_tourn_form'] = tournament_form
        context['is_tourn_admin'] = is_tourn_admin

    return render(request, 'tournament/main.html', context)


def create_tournament(request):
    if request.method == 'POST':
        tournament_form = NewTournament(request.POST)
        if tournament_form.is_valid():
            tournament_form.save()
            return redirect('main')


def create_teams(request):
    pass


def tournament(request, tournament_name):
    get_tournament = Tournament.objects.get(name=tournament_name)
    context = {'tournament': get_tournament}
    return render(request, 'tournament/tournament.html', context)


def table(request, stage_id, tournament_name):
    get_stage = Stage.objects.get(id=stage_id)
    context = {'stage': get_stage}
    if get_stage.mode == "PO":
        return render(request, 'tournament/table_po.html', context)
    else:
        return render(request, 'tournament/table_reg.html', context)


def edit_profile(request):
    if request.user.is_anonymous:
        return redirect('main')
    profile = Player.objects.get(user=request.user)
    full_name = '%s %s' % (profile.first_name, profile.last_name)
    context = {'profile': profile, 'full_name': full_name}
    return render(request, 'tournament/player_profile.html', context)


def about(request):
    return render(request, 'tournament/about.html')


def players(request):
    get_players = Player.objects.all()
    context = {'players': get_players}
    return render(request, 'tournament/players.html', context)
