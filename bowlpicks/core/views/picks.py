from django.shortcuts import render_to_response
from django.template import RequestContext  #, loader, Context

from django.views.generic.list import ListView
from bowlpicks.core.models import Season
from bowlpicks.profiles.models import Player


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

    return render_to_response(template_name, {
        'games': games,
        'season': season,
        'players': players
    }, context_instance=RequestContext(request))
