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
