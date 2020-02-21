from django.shortcuts import render
from django.views.generic import TemplateView


class FindView(TemplateView):
    template_name = "pages/find.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Find Help'
        return context

    def post(self, request, *args, **kwargs):
        pass
