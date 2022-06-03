from rest_framework import serializers

from .models import Site, Post, Item

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
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
            "item",
            "post",
        )
        model = Item