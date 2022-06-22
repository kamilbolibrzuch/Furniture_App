from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

#???????????? POBIERANIE 7 NAJNOWSZYCH NA STRONĘ GŁÓWNĄ ?????????????????#
class LatestPostsList(APIView):                                        #pobieranie ostatnio dodanych
    def get(self, request, format=None):
        posts = Post.objects.all()[0:7]                                #pobiera od 0 do 7 w kolejności od najnowszych
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

#^^^^^^^^^^^^^^^^^^^^^^^ DODAWANIE POSTÓW ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
