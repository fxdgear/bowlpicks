from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseForbidden
from django.template import RequestContext  #, loader, Context
from django.contrib.auth.decorators import login_required

from bowlpicks.profiles.forms import PlayerForm
from bowlpicks.profiles.models import Profile
from bowlpicks.core.models import Season


@login_required
def profile_detail(request, *args, **kwargs):
    template_name = "profiles/profile_detail.html"
    profile_id = kwargs.get('pk')
    profile = Profile.objects.get(pk=profile_id)
    if not profile == request.user.get_profile():
        return HttpResponseForbidden()

    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.profile = profile
            player.save()
            return redirect('bowlpicks_profile_detail', pk=profile.pk)
    else:
        form = PlayerForm()

    season = Season.objects.current()

    return render_to_response(template_name, {
        'form': form,
        'profile': profile,
        'season': season
    }, context_instance=RequestContext(request))
