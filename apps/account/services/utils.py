
from django.core.mail import send_mail
from account.serializers import ForgotSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


def post(self, request):
        serializer = ForgotSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            Please, confirm your email
            """
            return Response(message)
            
def get(self, request, activation_code):
        user = get_object_or_404(user, activation_code=activation_code)
        user.is_active=True
        user.activation_code=''
        user.save()
        return Response('Your account is successfully activated!')

def confirm_email(self):
    activation_url = f'http://127.0.0.1:8000/account/forgot_password/'
    message = f'''
        Confirm yout email {activation_url}
    '''
    send_mail('Confirm your email', message, 'test@mail.com', [self.email, ])
    return True