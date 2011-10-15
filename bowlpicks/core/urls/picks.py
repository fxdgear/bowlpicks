from django.conf.urls.defaults import patterns, url

from bowlpicks.core.views.picks import pick_list, pick_detail, create_pick

urlpatterns = patterns('',
    url(r'^$', pick_list, {}, 'pick_list'),
    url(r'^(?P<pk>\d+)/$', pick_detail, {}, 'pick_detail'),
    url(r'^create$', create_pick, {}, 'pick_create'),
)
