from django.conf.urls.defaults import patterns, include, url
from django.views.generic.detail import DetailView
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from django.contrib import admin
admin.autodiscover()

from bowlpicks.core.views import HomePage
from bowlpicks.profiles.models import Profile
from bowlpicks.profiles.views import profile_detail, delete_player


urlpatterns = patterns('',
    url(r'^$', HomePage.as_view(), {}, 'homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/password/reset/$',
        password_reset,
        {'template_name': 'registration/forgot_password.html'},
        name='password_reset'),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reset_done.html'}),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reset_done.html'}),
    url(r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'}),
    url(r'^reset/done/$',
        password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'}),
    url(r'^accounts/', include('registration.backends.default.urls')),
    (r'^contact/thankyou/$', 'bowlpicks.contact.views.thankyou'),
    (r'^contact/$', 'bowlpicks.contact.views.contactview', {}, 'contact'),
    (r'^contact/email_everyone/', 'bowlpicks.contact.views.email_everyone', {}, 'email_everyone'),
    url(r'^picks/', include('bowlpicks.core.urls.picks')),
    url(r'^profiles/(?P<pk>\d+)/$', profile_detail, {}, 'bowlpicks_profile_detail'),
    url(r'^profiles/(?P<pk>\d+)/picks$', DetailView.as_view(
                template_name="profiles/profile_picks.html",
                model=Profile), {}, 'profile_picks'),
    url(r'profiles/delete_player/(?P<player_id>\d+)/$', delete_player, {}, 'bowlpicks_delete_player'),
    url(r"^profiles/", include("idios.urls")),
)
