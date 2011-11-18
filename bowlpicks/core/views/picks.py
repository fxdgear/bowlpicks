from django.shortcuts import render_to_response
from django.template import RequestContext  #, loader, Context
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import ProcessFormView
from django.views.generic.base import View

from bowlpicks.core.models import Season, Game, Team, Pick
from bowlpicks.profiles.models import Player
from bowlpicks.core.forms import PickForm, PlayerForm


@login_required
def create_pick(request, *args, **kwargs):
    profile = request.user.get_profile()
    game_id = request.GET.get('game')
    player_id = request.GET.get('player')
    winner_id = request.GET.get('winner')

    try:
        player = profile.player_set.get(pk=player_id)
    except:
        return HttpResponseForbidden()

    if request.is_ajax and request.method == "GET":
        game = Game.objects.get(pk=game_id)
        season = game.season
        if season.is_froze:
            return HttpResponseForbidden()

        winner = Team.objects.get(pk=winner_id)
        pick, created = Pick.objects.get_or_create(game=game, player=player)
        pick.winner = winner
        pick.save()
        return HttpResponse(status=200)


def pick_list(request, *args, **kwargs):
    template_name = kwargs.pop('template', "pick/pick_list_new.html")
    season = Season.objects.filter(current=True)[0]
    games = season.game_set.all().order_by('date')
    player_list = [p for p in Player.objects.all() if p.active]
    players = []

    # create a list of tuples (player, player_picks) where player picks are odered
    # by game date to match the list of games above.
    for p in player_list:
        players.append((p, p.pick_set.curent_season().order_by('game__date')))

    players = sorted(players, key=lambda player: player[0].points, reverse=True)

    return render_to_response(template_name, {
        'games': games,
        'season': season,
        'players': players
    }, context_instance=RequestContext(request))


@login_required
def pick_detail(request, *args, **kwargs):
    template_name = kwargs.pop('template', 'pick/pick_detail.html')

    player_id = kwargs.pop('pk')
    player = Player.objects.get(pk=player_id)
    season = request.GET.get('season', None)
    if not season:
        picks = player.pick_set.curent_season()
        try:
            season = picks[0].game.season
        except:
            pass
    else:
        start, end = season.split("-")
        picks = player.pick_set.filter(game__season__year_start=start,
                                       game__season__year_end=end).order_by('game__date')

    return render_to_response(template_name, {
        'player': player,
        'picks': picks,
        'season': season
    }, context_instance=RequestContext(request))
