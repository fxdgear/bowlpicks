from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    topic = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class EmailForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
