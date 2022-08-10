from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from apps.api.models.user_models import User
from apps.api.serializers import UserSerializer


class UsersView(View):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

    # need to improve CSRF
    @csrf_exempt
    def post(self, request, *args, **kawrgs):
        print("POST")
