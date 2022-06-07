from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

from apps.order.serializers import OrderSerializer
from .models import Order
from apps.product.permissions import IsAdminOrAuthor



# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = (IsAuthenticated,)

class OrderListVIew(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)




class CreateOrderVIew(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrAuthor,)

class DestroyOrderVIew(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrAuthor, )

class RetrieveOrderVIew(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (AllowAny, )


class UpdateOrderVIew(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrAuthor, )