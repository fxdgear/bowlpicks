from django.db import models
import datetime
from django.http import HttpRequest
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
import urllib2

from bowlpicks.profiles.models import Player, PlayerRanking


class SeasonManager(models.Manager):
    def current(self):
        return self.filter(current=True)[0]


class Season(models.Model):
    year_start = models.CharField(max_length=10)
    year_end = models.CharField(max_length=10)
    current = models.BooleanField(default=False)
    freeze_date = models.DateField(blank=True, null=True)

    objects = SeasonManager()

    def __unicode__(self):
        return u"%s-%s" % (self.year_start, self.year_end)

    def leaders(self):
        return PlayerRanking.objects.filter(season=self)[:10]


    def get_picks(self):
        return Pick.objects.filter(game__season=self)

    @property
    def is_froze(self):
        return datetime.date.today() >= self.freeze_date


class Conference(models.Model):

    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=10)

    def __unicode__(self):
        return u"%s" % self.abbr


class School(models.Model):

    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=100)
    mascot = models.CharField(max_length=100)
    conference = models.ForeignKey(Conference)
    color = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        ordering = ['name', ]

    def __unicode__(self):
        return u"%s %s" % (self.name, self.mascot)


class Team(models.Model):

    school = models.ForeignKey(School)
    season = models.ForeignKey(Season)
    record = models.CharField(max_length=20)
    rank = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        """
        2011-2012 - Colorado State Rams (13-2-1)
        """
        return "%s - %s (%s)" % (self.season, self.school, self.record)

EST = 1
CST = 2
MST = 3
PST = 4
TIMEZONES = (
    (EST, "EST"),
    (CST, "CST"),
    (MST, "MST"),
    (PST, "PST"),
)


class GameManger(models.Manager):
    def today(self, *args, **kwargs):
        return self.filter(
            date__lt=datetime.datetime.today() + datetime.timedelta(days=1),
            date__gte=datetime.datetime.today()).order_by('date')

    def tomorrow(self, *args, **kwargs):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        return self.filter(
            date__lt=tomorrow + datetime.timedelta(days=1),
            date__gte=tomorrow).order_by('date')

def get_current_season():
    return Season.objects.current()

class Game(models.Model):
    date = models.DateTimeField()
    timezome = models.IntegerField(choices=TIMEZONES, default=EST)
    season = models.ForeignKey(Season, default=get_current_season())
    name = models.CharField(max_length=100)
    channel = models.CharField(max_length=100, default="Change Me")
    away_team = models.ForeignKey(Team, related_name="away_team", blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)
    home_team = models.ForeignKey(Team, related_name="home_team", blank=True, null=True)
    home_score = models.IntegerField(blank=True, null=True)

    require_tie_breaker = models.BooleanField(default=False)

    objects = GameManger()

    class Meta:
        ordering = ['date', ]

    def __unicode__(self):
        return u"(%s) %s" % (self.season, self.name)

    @property
    def short_name(self):
        return u"%s vs %s" % (self.home_team.school.abbr, self.away_team.school.abbr)

    def home_picks(self):
        return self.pick_set.filter(winner=self.home_team)

    def away_picks(self):
        return self.pick_set.filter(winner=self.away_team)

    def away_percent(self):
        try:
            value = (float(self.away_picks().count()) / float(self.pick_set.count())) * 100
        except ZeroDivisionError:
            value = 0
        return int(value)

    def home_percent(self):
        try:
            value = (float(self.home_picks().count()) / float(self.pick_set.count())) * 100
        except ZeroDivisionError:
            value = 0
        return int(value)

    @property
    def winner_home(self):
        return self.home_picks().count() > self.away_picks().count()

    @property
    def winner_away(self):
        return self.away_picks().count() > self.home_picks().count()

    @property
    def winner(self):
        if self.home_score > self.away_score:
            return self.home_team
        elif self.away_score > self.home_score:
            return self.away_team
        else:
            return None


class PickManager(models.Manager):
    def curent_season(self):
        season = Season.objects.filter(current=True)[0]
        return self.filter(game__season=season).order_by('game__date')


class Pick(models.Model):

    player = models.ForeignKey("profiles.Player")
    game = models.ForeignKey(Game)
    winner = models.ForeignKey(Team, blank=True, null=True)
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)

    objects = PickManager()

    def __unicode__(self):
        return u"%s - %s" % (self.player, self.winner)

    @property
    def correct(self):
        if self.winner:
            return self.winner == self.game.winner
        else:
            return None


def pick_post_save(sender, instance, signal, *args, **kwargs):
    pick = instance
    player = pick.player



def game_post_save(sender, instance, signal, *args, **kwargs):
    season = Season.objects.current()
    for player in Player.objects.all():
        rank, created = PlayerRanking.objects.get_or_create(
            season=season,
            player=player)

        rank.correct = player.points
        rank.wrong = player.wrong
        rank.save()


post_save.connect(pick_post_save, sender=Pick)
post_save.connect(game_post_save, sender=Game)
