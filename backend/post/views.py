from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post,Photo
from .serializers import PostSerializer,PostPhotosSerializer
from django.http import Http404
from rest_framework import status
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

#???????????? POBIERANIE 7 NAJNOWSZYCH NA STRONĘ GŁÓWNĄ ????????????????????????????????????????????????????????????????????????????????????????
class LatestPostsList(APIView):                                         #pobieranie ostatnio dodanych
    def get(self, request, format=None):
        posts = Post.objects.all()[0:7]                                #pobiera od 0 do 7 w kolejności od najnowszych
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

#^^^^^^^^^^^^^^^^^^^^^^^ DODAWANIE POSTÓW ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class AddPost(APIView):
    def post(self, request, *args, **kwargs):                               #dodawanie postów przez użytkownika
        data = self.request.data.copy()
        data['author'] = self.request.user.id                           #pobieramy id użytkownika (zalogowanego) który dodaje post, jako id authora
        serializer = PostSerializer(data=data)                          #standarrdowy serializer dla postów
        if serializer.is_valid():
            post = serializer.save()
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        #dodano
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)   #błędne dane
#!!!!!!!!!!!!!!!!!!!!!!POBIERANIE POSTÓW Z PAGINACJĄ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class GetPosts(APIView):
    def post(self, request, format=None):
        order_by = self.request.query_params.get('order_by')                            #pobieramy rodzaj sortowania postów
        if order_by == 'from-newest':
            posts = Post.objects.filter(Q(deleted=False))                                   #pobieramy tylko te które nie są usunięte
        if order_by == 'from-oldest':
            posts = Post.objects.filter(Q(deleted=False)).order_by('date_added')            #pobieramy tylko te które nie są usunięte od najstarszych
        if order_by == 'alphabetical':
            posts = Post.objects.filter(Q(deleted=False)).order_by('name')                  #pobieramy tylko te które nie są usunięte według nazwy   
        if order_by == 'alphabetical-reverse':
            posts = Post.objects.filter(Q(deleted=False)).order_by('-name')                 #pobieramy tylko te które nie są usunięte według nazwy (odwrócone od Z-A)          
        page_number = self.request.query_params.get('page_number', 1)                   #pobieramy z parametu numer strony aktualnie 1
        page_size = self.request.query_params.get('page_size', 10)                      #pobieramy ilość elementów na stronie aktualnie 10


        paginator = Paginator(posts, page_size)                                         #paginator sam dzieli ilość postów na podstawie page_size i zwraca aktualnie wybrane wyniki np pierwsze 10
        serializer = PostSerializer(paginator.page(page_number), many=True)
        data={}
        data['results'] = serializer.data                                               #zwracamy wwyniki
        data['page_numbers'] = paginator.num_pages                                      #zwracamy informacje ile wszystkich ,,podstron" jeszcze istnieje
        data['next_page'] = False if int(page_number) >= paginator.num_pages else True  #zwracamy informacje że istnieje kolejna podstrona do której możemy przejść
        return Response(data, status=status.HTTP_200_OK)                                #poprawnie pobrano
#**********************POBIERANIE KONKRETNEGO POSTU NA PODSTAWIE SLUG'A *************************************************************************
class PostDetail(APIView):
    def get_object(self, post_slug):
        try:
            return Post.objects.get(slug=post_slug)
        except Post.DoesNotExist:
            raise Http404
    def get(self, request, post_slug, format=None):
        post = self.get_object(post_slug)
        print(post)
        serializer = PostSerializer(post)
        return Response(serializer.data, status.HTTP_200_OK)


#~~~~~~~~~~~~~~~~~~~~~~~DODAWANIE ZDJĘĆ DO POSTÓW ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AddPostImages(APIView):
    def post(self, request, format=None):
        post = Post.objects.latest('id').id                         #dodaje do ostatnio dodanego postu (ostatnie id)
        images=request.FILES.getlist('image')                       #tworzy listę zdjęć
        img_table = []                                              #tablica na obiekty
        for image in images:                                        #dla każdego zdjęcia
            post_photo = Photo.objects.create(                      #tworzy nowy obiekt zdjęcia
                post=Post.objects.latest('id'),
                image=image,
                name=image.name)
            post_photo.save()                                        #zapisuje go
            img_table.append(post_photo)                             #dodaje obiekty do tablicy
            
        serializer = PostPhotosSerializer(img_table,many=True )      #serializuje
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        