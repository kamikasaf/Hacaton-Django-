from django.shortcuts import render, get_list_or_404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import HttpResponse

from .serializers import *
from .models import send_new_password

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


class ForgotPasswordView(APIView):


    def post(self, request):
        data = request.POST
        serializer = ForgotSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        user: CustomUser = CustomUser.objects.get(email=email)
        new_password=user.password = user.generate_activation_code()
        user.set_password(new_password)
        user.save()
        send_new_password(email, new_password)
        return Response(f'message: Your new password send in your {email}', status=status.HTTP_200_OK)