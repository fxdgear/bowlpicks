from django.conf.urls.defaults import patterns, url
from django.views.generic.detail import DetailView

from bowlpicks.profiles.models import Profile


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(
                model=Profile), {}, 'profile_detail'),
    url(r'^(?P<pk>\d+)/picks$', DetailView.as_view(
                template_name="profiles/profile_picks.html",
                model=Profile), {}, 'profile_picks'),
)
