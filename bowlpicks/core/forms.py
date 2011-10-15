from django import forms
from django.contrib.formtools.wizard import FormWizard
from django.shortcuts import render_to_response

from bowlpicks.core.models import Pick


class PlayerForm(forms.Form):
    players = forms.ChoiceField()

    def __init__(self, players=None, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['players'].choices = [(x.pk, x.name) for x in players]


class PickForm(forms.ModelForm):

    def __init__(self, game, player, *args, **kwargs):
        super(PickForm, self).__init__(*args, **kwargs)
        self.fields['game'].initial = game
        self.fields['player'].initial = player

    class Meta:
        model = Pick


class PickWizard(FormWizard):
    def done(self, request, form_list):
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

