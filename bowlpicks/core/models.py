from django.db import models


class Season(models.Model):
    year_start = models.CharField(max_length=10)
    year_end = models.CharField(max_length=10)

    def __unicode__(self):
        return u"%s-%s" % (self.year_start, self.year_end)


class Conference(models.Model):

    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=10)

    def __unicode__(self):
        return u"%s" % self.name


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

    def __unicode__(self):
        """
        2011-2012 - Colorado State Rams (13-2-1)
        """
        return "%s - %s (%s)" % (self.season, self.school, self.record)


class Game(models.Model):
    date = models.DateTimeField()
    season = models.ForeignKey(Season)
    name = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    away_team = models.ForeignKey(Team, related_name="away_team")
    away_score = models.IntegerField(blank=True, null=True)
    home_team = models.ForeignKey(Team, related_name="home_team")
    home_score = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name


class Pick(models.Model):

    profile = models.ForeignKey("profiles.Profile")
    game = models.ForeignKey(Game)
    winner = models.ForeignKey(School)
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)

    is_tie_breaker = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s - %s" % (self.profile, self.winner)
