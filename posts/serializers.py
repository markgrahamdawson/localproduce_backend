from rest_framework import serializers

from .models import Site, Post, Item

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "description",
            "lat",
            "lon",
            "author",
            "created_at",
        )
        model = Site

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "message",
            "author",
            "site",
            "created_at",
            "image",
        )
        model = Post

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "item",
            "post",
        )
        model = Item




class PostSerializerExtended(serializers.ModelSerializer):
    items = ItemSerializer(source='item_set', many=True)
    class Meta:
        fields = (
            "id",
            "message",
            "author",
            "site",
            "created_at",
            "image",
            "items",
        )
        model = Post

class SiteSerializerExtended(serializers.ModelSerializer):
    posts = PostSerializerExtended(source='post_set', many=True)
    class Meta:
        fields = (
            "id",
            "name",
            "description",
            "lat",
            "lon",
            "author",
            "created_at",
            "posts"
        )
        model = Site

