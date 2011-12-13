from django.db import models
from django.db.models import get_model

from idios.models import ProfileBase


class Profile(ProfileBase):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        if self.first_name or self.last_name:
            return u"%s" % self.full_name
        else:
            return self.user.username

    def current_season(self):
        model = get_model('core', 'Season')
        return model.objects.current()


class Player(models.Model):
    profile = models.ForeignKey(Profile)
    name = models.CharField(max_length=100, unique=True)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

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
    def wrong(self):
        count = 0
        for p in self.pick_set.curent_season():
            if not p.correct:
                count += 1
        return count
