from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post,Photo
from .serializers import PostSerializer,PostPhotosSerializer
from django.http import Http404
from rest_framework import status
from datetime import datetime

from django.shortcuts import render, get_object_or_404

#???????????? POBIERANIE 7 NAJNOWSZYCH NA STRONĘ GŁÓWNĄ ?????????????????#
class LatestPostsList(APIView):                                        #pobieranie ostatnio dodanych
    def get(self, request, format=None):
        posts = Post.objects.all()[0:7]                                #pobiera od 0 do 7 w kolejności od najnowszych
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

#^^^^^^^^^^^^^^^^^^^^^^^ DODAWANIE POSTÓW ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class PostsListView(APIView):
    def post(self, request, *args, **kwargs):                               #dodawanie postów przez użytkownika
        data = self.request.data.copy()
        data['author'] = self.request.user.id                           #pobieramy id użytkownika (zalogowanego) który dodaje post, jako id authora
        serializer = PostSerializer(data=data)                          #standarrdowy serializer dla postów
        if serializer.is_valid():
            post = serializer.save()
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        #dodano
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)   #błędne dane

class PostImagesListView(APIView):
    def post(self, request, format=None):
        post = Post.objects.latest('id').id
        images=request.FILES.getlist('image')
        
        img_table = []
        for image in images:
            post_photo = Photo.objects.create(
                post=Post.objects.latest('id'),
                image=image,
                name=image.name)
            post_photo.save()
            img_table.append(post_photo)
            
        serializer = PostPhotosSerializer(img_table,many=True )
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)