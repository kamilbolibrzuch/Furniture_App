from django.db.models import fields
from rest_framework import serializers
from .models import Post, Image
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
            images = Image.objects.filter(post=obj.id, deleted=False).all()
            return PostImagesSerializer(images, many=True).data
        except:
            return ''

class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
