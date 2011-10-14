from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return u"%s" % self.full_name


class Player(models.Model):
    profile = models.ForeignKey(Profile)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.name

    @property
    def points(self):
        points = 0
        for p in self.pick_set.curent_season():
            if p.correct:
                points += 1
        return points

    @property
    def active(self):
        return self.pick_set.curent_season().count()
