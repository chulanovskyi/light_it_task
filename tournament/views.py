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
    is_tourn_admin = request.user.groups.filter(name='tournament_admin').exists()
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
    Tournament.objects.filter(id=tournament_id).delete()
    return redirect('main')


def create_teams(request, tournament_id):
    if Team.objects.filter(tournament_id=tournament_id).exists():
        return redirect('main')
    tournament = Tournament.objects.get(id=tournament_id)
    players = tournament.players.all().order_by('rank')
    half = int(len(players)/2)
    weak, strong = (players[:half], players[half:])
    while weak:
        if random.random() > 0.8:
            p1 = weak.pop(random.randrange(len(weak)))  # need to rid of len
            p2 = strong.pop(random.randrange(len(strong)))
        else:
            p1 = weak.pop(0)
            p2 = strong.pop()
        team_name = '{p1_f} {p1_l} | {p2_f} {p2_l}'.format(
            p1_f=p1.first_name,
            p1_l=p1.last_name,
            p2_f=p2.first_name,
            p2_l=p2.last_name,)
        team = Team(name=team_name, tournament=tournament)
        team.save()  # maybe there is better way without using save() two times
        team.players.add(p1, p2)
        team.save()
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
    social_acc = request.user.socialaccount_set.all().first()
    if social_acc:
        social_ava = social_acc.get_avatar_url()
        context['social_ava'] = social_ava
    return render(request, 'tournament/player_profile.html', context)


def about(request):
    return render(request, 'tournament/about.html')


def players(request):
    get_players = Player.objects.all()
    context = {'players': get_players}
    return render(request, 'tournament/players.html', context)
