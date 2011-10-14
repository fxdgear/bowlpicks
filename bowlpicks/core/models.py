from django.db import models
import datetime


class Season(models.Model):
    year_start = models.CharField(max_length=10)
    year_end = models.CharField(max_length=10)
    current = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s-%s" % (self.year_start, self.year_end)


class Conference(models.Model):

    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=10)

    def __unicode__(self):
        return u"%s" % self.abbr


class School(models.Model):

    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=10)
    mascot = models.CharField(max_length=100)
    conference = models.ForeignKey(Conference)

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
        return self.all()
        #return self.filter(date=datetime.datetime.today()).order_by('-date')


class Game(models.Model):
    date = models.DateTimeField()
    timezome = models.IntegerField(choices=TIMEZONES)
    season = models.ForeignKey(Season)
    name = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    away_team = models.ForeignKey(Team, related_name="away_team")
    away_score = models.IntegerField(blank=True, null=True)
    home_team = models.ForeignKey(Team, related_name="home_team")
    home_score = models.IntegerField(blank=True, null=True)

    objects = GameManger()

    def __unicode__(self):
        return u"(%s) %s" % (self.season, self.name)

    def home_picks(self):
        return self.pick_set.filter(winnner=self.home_team)

    def away_picks(self):
        return self.pick_set.filter(winner=self.away_team)

    @property
    def winner_home(self):
        return self.home_picks > self.away_picks

    @property
    def winner_away(self):
        return self.away_picks > self.home_picks

    @property
    def winner(self):
        if self.home_score > self.away_score:
            return self.home_team
        else:
            return self.away_team


class Pick(models.Model):

    player = models.ForeignKey("profiles.Player")
    game = models.ForeignKey(Game)
    winner = models.ForeignKey(Team)
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)

    is_tie_breaker = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s - %s" % (self.player, self.winner)
