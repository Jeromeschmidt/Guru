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
        # min_rent = Person.objects.get(model.first_name = request.user.username)
        # print(min_rent)
        # max_rent = None
        helpers = self.get().all()#.order_by('-pub_date')
        print('!!!!')
        return render(request, "pages/find_help.html", {
          'helpers': helpers
        })

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context["title"] = "Find Help"
        # # context["topics"] = (None,) * 8
        # # context["topics"] = ("yes", "no") # * 8
        # topics = ["yes", "no"]
        # # # context["algolia-api-key"] = env("ALGOLIA_API_KEY")
        # return topics

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
