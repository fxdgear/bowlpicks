from django.views.generic import TemplateView


class HomePage(TemplateView):
    template = "homepage.html"
