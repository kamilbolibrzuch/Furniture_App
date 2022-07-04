from django.urls import path, include
from .views import LatestPostsList,AddPost,PostDetail,GetPosts
from post import views
urlpatterns = [
    path('latest-posts/', views.LatestPostsList.as_view(), name = 'get, return newest/latests posts'),  #GET zwraca ostatnio dodane posty
    path('add-post/', views.AddPost.as_view(), name = 'post, add new post'),                            #* POST dodawanie nowych postów
    path('add-post/image/', views.AddPostImages.as_view(), name = 'post, add multiple images to post'), #* POST dodawanie zdjeć do postu
    path('posts/', views.GetPosts.as_view(), name = 'get, return posts with pagination'),                          #GET pobieranie postów z paginacja
    path('post/<slug:post_slug>/', views.PostDetail.as_view(), name = 'get, return post details'),      #GET pobieranie szczęgółów posta

]