from django.shortcuts import render, redirect
from .models import Tournament, Stage, Player, Team
from .forms import NewTournament, NewStage
from django.views.decorators.http import require_POST
import random


def main(request):
    tournaments = Tournament.objects.all()
    context = {
        'tournaments': tournaments,
    }
    is_tourn_admin = request.user.groups.filter(name='tournament_admin')
    if is_tourn_admin:
        tournament_form = NewTournament()
        stage_form = NewStage()
        context['new_tourn_form'] = tournament_form
        context['is_tourn_admin'] = is_tourn_admin
        context['new_stage_form'] = stage_form
    return render(request, 'tournament/main.html', context)


@require_POST
def create_tournament(request):
    tournament_form = NewTournament(request.POST)
    if tournament_form.is_valid():
        tournament_form = tournament_form.save()
        stage_form = NewStage(request.POST)
        new_tournament_id = stage_form.save(commit=False)
        new_tournament_id.tournament_id = tournament_form.id
        new_tournament_id.save()
        stage_form.save()
    return redirect('main')


def delete_tournament(request, tournament_id):
    tourn = Tournament.objects.get(id=tournament_id)
    tourn.delete()
    return redirect('main')


def create_teams(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    players = tournament.players.all()
    if Team.objects.filter(tournament_id=tournament_id):  # проверка на наличие команд в данном турнире
        pass
    else:
        players_list = []
        for player in players:
            players_list.append('{0} {1}'.format(player.first_name, player.last_name))
        teams = []
        random.shuffle(players_list) #перемешал список плееров
        while True:
            try:
                player_one = players_list.pop()
                player_two = players_list.pop()
            except IndexError:
                break
            team = [player_one, player_two]
            teams.append(team)
            team = []
        for team in teams:
            team_create = Team(name='{0} {1}'.format(*team), tournament=tournament)
            team_create.save()
    return redirect('main')


def tournament(request, tournament_name):
    get_tournament = Tournament.objects.get(name=tournament_name)
    context = {'tournament': get_tournament}
    return render(request, 'tournament/tournament.html', context)


def table(request, tournament_name, stage_id):
    get_stage = Stage.objects.get(id=stage_id)
    tournament_id = get_stage.tournament_id
    teams = Team.objects.filter(tournament_id=tournament_id)
    context = {
        'stage': get_stage,
        't_name': tournament_name,
        'teams': teams
    }
    if get_stage.mode == "PO":
        return render(request, 'tournament/table_po.html', context)
    else:
        return render(request, 'tournament/table_reg.html', context)


def edit_profile(request):
    if request.user.is_anonymous:
        return redirect('main')
    player = Player.objects.get(user=request.user)
    full_name = '%s %s' % (player.first_name, player.last_name)
    context = {'player': player, 'full_name': full_name}
    social_acc = request.user.socialaccount_set.all()
    if social_acc:
        social_ava = social_acc[0].get_avatar_url()
        context['social_ava'] = social_ava
    return render(request, 'tournament/player_profile.html', context)


def about(request):
    return render(request, 'tournament/about.html')


def players(request):
    get_players = Player.objects.all()
    context = {'players': get_players}
    return render(request, 'tournament/players.html', context)
