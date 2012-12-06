from django.contrib import admin
from bowlpicks.profiles.models import Profile, Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile', 'season', 'paid', 'active']
    list_edit = ['paid', 'active']

class PlayerInline(admin.TabularInline):
    model = Player

class ProfileAdmin(admin.ModelAdmin):
    inlines = [PlayerInline, ]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Player, PlayerAdmin)
