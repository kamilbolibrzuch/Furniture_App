from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.http import Http404
from rest_framework import status

#???????????? POBIERANIE 7 NAJNOWSZYCH NA STRONĘ GŁÓWNĄ ?????????????????#
class LatestPostsList(APIView):                                        #pobieranie ostatnio dodanych
    def get(self, request, format=None):
        posts = Post.objects.all()[0:7]                                #pobiera od 0 do 7 w kolejności od najnowszych
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

#^^^^^^^^^^^^^^^^^^^^^^^ DODAWANIE POSTÓW ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class AddPosts(APIView):
    def post(self, request, format=None):                               #dodawanie postów przez użytkownika
        data = self.request.data
        data['author'] = self.request.user.id                           #pobieramy id użytkownika (zalogowanego) który dodaje post, jako id authora
        serializer = PostSerializer(data=data)                          #standarrdowy serializer dla postów
        if serializer.is_valid():
            post = serializer.save()
            if 'image' in data:
                post.image = data['image']
                post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        #dodano
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)   #błędne dane