from django.conf.urls.defaults import patterns, url

from bowlpicks.core.views.picks import pick_list, pick_detail

urlpatterns = patterns('',
    url(r'^$', pick_list, {}, 'pick_list'),
    url(r'^(?P<pk>\d+)/$', pick_detail, {}, 'pick_detail'),
)
