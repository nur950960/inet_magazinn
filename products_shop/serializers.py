from rest_framework import serializers
from .models import Products  

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        post = super().create(validated_data)
        post.save()
        return post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('title','image','author')
