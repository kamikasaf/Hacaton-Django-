from .models import Product
from rest_framework import serializers
from apps.review.serializers import ReviewSerializer

class Produclserializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('author',)

    def validate(self, attrs):
            request = self.context.get('request')
            attrs['author'] = request.user
            return attrs
    
    def to_representation(self, instance):
        representation=super().to_representation(instance)
        representation['author'] = instance.author.name
        representation["category"] = instance.category.title
        representation["reviews"] = instance.reviews.all().count()
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        representation['likes']=instance.likes.filter(is_liked=True).count()
        representation['favorite']=instance.favorite.filter(favorite=True).count()
        return representation

