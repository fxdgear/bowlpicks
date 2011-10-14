from django.views.generic import TemplateView
from bowlpicks.core.models import Season


class HomePage(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        # filter by current season, and grab the first one.
        # must make sure there is only ever one season marked as current.
        season = Season.objects.filter(current=True)[0]
        context['games'] = season.game_set.today()
        return context
