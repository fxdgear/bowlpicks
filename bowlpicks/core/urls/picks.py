from django.conf.urls.defaults import patterns, url

from bowlpicks.core.views.picks import pick_list

urlpatterns = patterns('',
    url(r'^$', pick_list, {}, 'pick_list'),
)
