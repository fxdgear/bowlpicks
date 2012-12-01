from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.template import RequestContext  #, loader, Context
from django.contrib.auth.decorators import login_required

from bowlpicks.profiles.forms import PlayerForm
from bowlpicks.profiles.models import Profile, Player
from bowlpicks.core.models import Season, Game, Pick


@login_required
def profile_detail(request, *args, **kwargs):
    template_name = "profiles/profile_detail.html"
    profile_id = kwargs.get('pk')
    profile = Profile.objects.get(pk=profile_id)
    if not profile == request.user.get_profile():
        return HttpResponseForbidden()

    if request.method == "POST":
        initial={'profile': profile.pk, 'active': False}
        form = PlayerForm(request.POST, initial=initial)
        if form.is_valid():
            player = form.save(commit=False)
            player.profile = profile
            player.save()
            player.season.add(Season.objects.current())
            return redirect('bowlpicks_profile_detail', pk=profile.pk)
        else:
            return render_to_response(template_name, {
                'form': form,
                'profile': profile,
            }, context_instance=RequestContext(request))

    else:
        form = PlayerForm()

    season = Season.objects.current()

    return render_to_response(template_name, {
        'form': form,
        'profile': profile,
        'season': season
    }, context_instance=RequestContext(request))


@login_required
def delete_player(request, *args, **kwargs):
    player_id = kwargs.get('player_id')
    player = Player.objects.get(pk=player_id)
    profile = request.user.get_profile()

    if not player in profile.player_set.all():
        return HttpResponseForbidden()
    else:
        player.delete()
        return redirect('bowlpicks_profile_detail', pk=profile.pk)

@login_required
def make_player_current(request, *args, **kwargs):
    """
    add current season to players list of seasons
    """

    player_id = player_id = kwargs.get('player_id')
    profile = request.user.get_profile()
    player = Player.objects.get(pk=player_id)

    if not player in profile.player_set.all():
        return HttpResponseForbidden()
    else:
        season = Season.objects.current()
        player.season.add(season)
        games = Game.objects.filter(season=season)
        for game in games:
            Pick.objects.create(player=player, game=game)

        return redirect('bowlpicks_profile_detail', pk=profile.pk)

