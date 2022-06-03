from django.shortcuts import render, get_list_or_404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import HttpResponse

from .serializers import UserSerializer, RegistrationSerializer, User

class LoginAPIView(APIView):

    def post(self,request):
        data = request.POST
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data.get('user')
            token, object = Token.objects.get_or_create(user=user)
            return Response({'Token': token.key})


class LogoutAPIView(APIView):

    def get(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()  
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            You are done!
            Please, confirm your email
            """
            return Response(message)

class ActivationView(APIView):
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active=True
        user.activation_code=''
        user.save()
        return Response('Your account is successfully activated!')