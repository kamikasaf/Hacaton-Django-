from django.urls import path

from apps.account.views import *

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]
