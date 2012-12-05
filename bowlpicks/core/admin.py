from django.contrib import admin
from bowlpicks.core.models import Season, Conference, School, Team, Game, Pick
from bowlpicks.core import listeners


class GameAdmin(admin.ModelAdmin):
    list_filter = ('season__year_end', )
    list_display = (
        'name',
        'date',
        'season',
        'home_team',
        'home_score',
        'away_team',
        'away_score',)
    raw_id_fields = ['home_team', 'away_team']
    search_fields = ['home_team', 'away_team']


class PickAdmin(admin.ModelAdmin):
    list_filter = ('player__name', 'game__season__year_end', 'game__name', )
    list_display = ('player', 'game', 'winner', )


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('year_start', 'year_end', 'current', 'freeze_date')


class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('abbr', 'name')


class TeamInline(admin.TabularInline):
    model = Team



class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr', 'mascot', 'conference', 'color')
    inlines = [TeamInline, ]
    list_editable = ('color',)
    search_fields = ['name', ]


class TeamAdmin(admin.ModelAdmin):
    list_display = ('school', 'season', 'record', 'rank')
    list_filter = ('season', )
    raw_id_fields = ['school', ]
    search_fields = ['school', ]
    list_editable = ('season',)


admin.site.register(Season, SeasonAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Pick, PickAdmin)
