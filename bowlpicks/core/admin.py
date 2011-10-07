from django.contrib import admin
from bowlpicks.core.models import Season, Conference, School, Team, Game, Pick

admin.site.register(Season)
admin.site.register(Conference)
admin.site.register(School)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Pick)
