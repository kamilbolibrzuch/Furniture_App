from django.urls import path, include
from .views import LatestPostsList,PostsListView
from post import views
urlpatterns = [
    path('latest-posts/', views.LatestPostsList.as_view()), #GET zwraca ostatnio dodane posty
    path('add-post/', views.PostsListView.as_view()), #dodawanie nowych postów
    path('add-post/image/', views.PostImagesListView.as_view()), #dodawanie zdjec do postu

]