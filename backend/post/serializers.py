from django.db.models import fields
from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "deleted",
            "date_added",
            "author",
            "name",
            "description",
            "slug",
            "get_absolute_url",
            "get_image",
            "get_thumbnail"
        )