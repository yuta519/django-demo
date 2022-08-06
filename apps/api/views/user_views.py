from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from apps.api.models.user_models import User

# Create your views here.


@csrf_exempt
def fetch_users(request):
    """
    return users
    """
    if request.method == 'GET':
        users = User.objects.all()
        return HttpResponse(users)
