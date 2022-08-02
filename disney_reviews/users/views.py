from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

from users.models import Users
from users.serializers import UsersSerializers
from rest_framework.decorators import api_view


User = get_user_model()

def index(request):
    return HttpResponse("Hello, world. You are at the users index.")

class reviews_list(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'templates/users/users_list.html'

    def get(self, request):
        queryset = Users.objects.all()
        return Response({'reviews': queryset})


@api_view(['POST'])
def add_user(request):
    users_data = JSONParser().parse(request)
    users_serializer = UsersSerializers(data=users_data)
    if users_serializer.is_valid():
        users_serializer.save()
        return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)