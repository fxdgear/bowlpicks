from django.conf.urls.defaults import patterns, include, url
from django.views.generic.detail import DetailView

from django.contrib import admin
admin.autodiscover()

from bowlpicks.core.views import HomePage
from bowlpicks.profiles.models import Profile
from bowlpicks.profiles.views import profile_detail


urlpatterns = patterns('',
    url(r'^$', HomePage.as_view(), {}, 'homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^picks/', include('bowlpicks.core.urls.picks')),
    url(r'^profiles/(?P<pk>\d+)/$', profile_detail, {}, 'bowlpicks_profile_detail'),
    url(r'^profiles/(?P<pk>\d+)/picks$', DetailView.as_view(
                template_name="profiles/profile_picks.html",
                model=Profile), {}, 'profile_picks'),
    url(r"^profiles/", include("idios.urls"))
)
