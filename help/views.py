from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponse

# from config.settings import env


#@login_required
class FindHelpView(TemplateView):
    template_name = "pages/find_help.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Find Help"
        # context["topics"] = (None,) * 8
        # context["topics"] = ("yes", "no") # * 8
        topics = ["yes", "no"]
        # # context["algolia-api-key"] = env("ALGOLIA_API_KEY")
        return topics

    def post(self, request, *args, **kwargs):
                return HttpResponse(render(request, 'pages/find_help.html',
                   {}))

class ConfirmationView(TemplateView):
    template_name = "pages/confirmation.html"

    def post(self, request, *args, **kwargs):
                return HttpResponse(render(request, 'pages/confirmation.html',
                   {}))
