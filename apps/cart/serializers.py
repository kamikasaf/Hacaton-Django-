from itertools import product
from requests import request
from rest_framework import serializers

from apps.cart.models import CartItem, ShoppingCart
from apps.product.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("id", "product", "quantity")

    def validate(self, attrs):
        cart_shopping = self.context.get("request").user.cart
        attrs['cart_shopping'] = cart_shopping
        return attrs

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['product'] = instance.product.title
            rep['total_price'] = instance.get_total_price_item()
            return rep
        except:
            return rep

    # def create(self, validated_data):
    #     cart = self.context.get("request").user.cart
    #     product = validated_data.get('product')
    #     quantity = validated_data.get('quantity')
    #     return CartItem.objects.create(cart_shopping=cart, product=product, quantity=quantity)


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['products'] = CartItemSerializer(instance.cart_item.all(), many=True).data
            rep['total_price'] = instance.get_total_all_price()
            return rep
        except:
            return rep
