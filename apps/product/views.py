
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.filters import OrderingFilter
import django_filters.rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import django_filters.rest_framework as filters
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from .models import Product
from .permissions import IsAdminOrAuthor
from .serializers import Produclserializers





class ListProductVIew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Produclserializers
    permission_classes = (AllowAny, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["price", "title", "author"]
    search_fields = ['title', 'price']
    ordering_fields = ['update_date']
    


class CreateProductVIew(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Produclserializers
    permission_classes = (AllowAny,)



class DestroyProductVIew(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Produclserializers
    permission_classes = (IsAdminOrAuthor, )

class RetrieveProductVIew(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = Produclserializers
    permission_classes = (AllowAny, )


class UpdateProductVIew(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = Produclserializers
    permission_classes = (IsAdminOrAuthor, )
