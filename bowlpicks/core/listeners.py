from django.db.models.signals import post_save

from bowlpicks.core.models import Season, Game, Pick
from bowlpicks.profiles.models import Player


def create_pick_for_players(sender, **kwargs):
    if kwargs.get('created'):
        game = kwargs.get('instance')
        for player in Player.objects.all():
            Pick.objects.create(player=player, game=game)


def create_pick_set_for_player(sender, **kwargs):
    if kwargs.get('created'):
        season = Season.objects.filter(current=True)[0]
        games = Game.objects.filter(season=season)
        player = kwargs.get('instance')
        for game in games:
            Pick.objects.create(player=player, game=game)

post_save.connect(create_pick_set_for_player, sender=Player)
post_save.connect(create_pick_for_players, sender=Game)
