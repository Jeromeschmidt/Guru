from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponse

from guru.users.models import User

# from config.settings import env


#@login_required
class FindHelpView(TemplateView):
    template_name = "pages/find_help.html"

    def get(self, request):
        """ GET a list of Pages. """
        helpers = self.get().all()#.order_by('-pub_date')
        return render(request, "pages/find_help.html", {
          'helpers': helpers
        })

    def post(self, request, *args, **kwargs):
        helpers = User.objects.all()
        skill_list = list()
        for e in helpers:
            try:
                for skill in e.skills:
                    if skill not in skill_list:
                        skill_list.append(skill)
            except:
                pass
        print(skill_list)
        return HttpResponse(render(request, 'pages/find_help.html',
           {'skill_list': skill_list}))

class ConfirmationView(TemplateView):
    template_name = "pages/confirmation.html"

    def post(self, request, *args, **kwargs):
                return HttpResponse(render(request, 'pages/confirmation.html',
                   {}))
