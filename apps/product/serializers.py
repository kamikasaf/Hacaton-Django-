from .models import Product
from rest_framework import serializers

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
        # representation["reviews"] = instance.reviews.all().count()
        return representation

