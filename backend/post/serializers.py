from django.db.models import fields
from rest_framework import serializers
from .models import Post, Photo
class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

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
            "image",
            "get_absolute_url",

        )

    def get_image(self,obj):
        try:
            images = Photo.objects.filter(post=obj.id, deleted=False).all()
            return PostPhotosSerializer(images, many=True).data
        except:
            return ''

class PostPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "id",
            "created",
            "edited",
            "name",
            "slug",
            "deleted",
            "get_image",
            "get_thumbnail",
            "post",
        )
