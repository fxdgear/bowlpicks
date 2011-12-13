from django.contrib import admin
from bowlpicks.profiles.models import Profile, Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile', 'paid', ]

admin.site.register(Profile)
admin.site.register(Player, PlayerAdmin)
