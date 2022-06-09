
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
import django_filters.rest_framework as filters
from rest_framework.response import Response

import django_filters.rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action


from apps.likes.models import Likes
from apps.product.pagiantions import ProductPagination
from .models import Product
from .permissions import IsAdminOrAuthor
from .serializers import Produclserializers





class ListProductVIew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Produclserializers
    permission_classes = (AllowAny, )
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["price", "title", "author", 'category']
    search_fields = ['title', 'price']
    order_fields = ['update_date']

    


class CreateProductVIew(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Produclserializers
    permission_classes = (IsAuthenticated,)



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
