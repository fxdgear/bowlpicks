from django.contrib import admin
from bowlpicks.profiles.models import Profile, Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile', 'paid', 'active']
    list_editable = ['paid', 'active']

class PlayerInline(admin.TabularInline):
    model = Player

class ProfileAdmin(admin.ModelAdmin):
    inlines = [PlayerInline, ]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Player, PlayerAdmin)
