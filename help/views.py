from django.shortcuts import render
from django.views.generic import TemplateView

class FindView(TemplateView):
    template_name = "pages/find.html"
