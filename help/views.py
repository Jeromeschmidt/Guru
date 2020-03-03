from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponse, QueryDict

from guru.users.models import User
from django.core.mail import send_mail as django_send_mail
from twilio.rest import Client
# from .forms import NameForm
import os
from dotenv import load_dotenv
load_dotenv()
# from config.settings import env
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

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
        return HttpResponse(render(request, 'pages/find_help.html',
           {'skill_list': skill_list}))

class ConfirmationView(TemplateView):
    template_name = "pages/confirmation.html"

    def get(self, request):
        # # form = NameForm(request.POST)
        # # django_send_mail('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
        # subject = request.GET['skill_list-options']
        # message = "I need help with " + subject
        # sender = "jerome.schmidt@students.makeschool.com"
        # # cc_myself = form.cleaned_data['cc_myself']
        #
        # # recipients = [user.email]
        # # if cc_myself:
        # #     recipients.append(sender)
        # twilioClient = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # # client.messages.create(to='+14028407963',
        # #                        from_='+18044915709',
        # #                        body=message)
        # message = twilioClient.messages.create(body="Another purchase!", from_='+18044915709', to='+14028407963')
        # # django_send_mail(subject, message, sender, recipients)
        subject = request.GET['skill_list-options']
        message = "I need help with " + subject
        twilioClient = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = twilioClient.messages.create(body=message, from_='+18044915709', to='+14028407963')
        return HttpResponse(render(request, 'pages/confirmation.html',
           {}))


    def post(self, request, *args, **kwargs):
        subject = request.GET['skill_list-options']
        message = "I need help with " + subject
        twilioClient = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = twilioClient.messages.create(body=message, from_='+18044915709', to='+14028407963')

        return HttpResponse(render(request, 'pages/confirmation.html',
           {}))

class MatchView(TemplateView):
    template_name = "pages/match.html"

    def get(self, request):

        return HttpResponse(render(request, 'pages/match.html',
           {}))


    def post(self, request, *args, **kwargs):
        return HttpResponse(render(request, 'pages/match.html',
           {}))
