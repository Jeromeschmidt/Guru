# from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from guru.users.models import User
from api.serializers import UserSerializer
# from api.serializers import ChoiceSerializer


class UserList(APIView):

    def get(self, request):
        user = User.objects.all()[:20]
        data = UserSerializer(user, many=True).data
        return Response(data)


class UserDetail(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = UserSerializer(user).data
        return Response(data)

# events/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
### help with slack bot: https://medium.com/freehunch/how-to-build-a-slack-bot-with-python-using-slack-events-api-django-under-20-minute-code-included-269c3a9bf64e
from rest_framework import status
from django.conf import settings
from slack import WebClient


SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings, 'SLACK_BOT_USER_TOKEN', None)                                     #
Client = WebClient(SLACK_BOT_USER_TOKEN)

class Events(APIView):
    def post(self, request, *args, **kwargs):

        slack_message = request.data

        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # verification challenge
        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message,
                            status=status.HTTP_200_OK)
        # greet bot
        if 'event' in slack_message:                              #4
            event_message = slack_message.get('event')            #

            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message':     #5
                return Response(status=status.HTTP_200_OK)        #

            # process user's message
            user = event_message.get('user')                      #6
            text = event_message.get('text')                      #
            channel = event_message.get('channel')                #
            bot_text = 'Hey <@{}> :wave:'.format(user)             #
            if 'hi' in text.lower():
                Client.chat_postMessage(
                    channel=channel,
                    text=bot_text
                    )                            #7
                # Client.api_call('chat.postMessage', event_message.get('channel'), bot_text)        #8
                                # channel=channel,                  #
                                # text=bot_text)
                                                #
                return Response(status=status.HTTP_200_OK)        #9

        return Response(status=status.HTTP_200_OK)
