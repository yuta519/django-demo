from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from apps.api.models.user_models import User
from apps.api.serializers import UserSerializer


class UsersView(View):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)
