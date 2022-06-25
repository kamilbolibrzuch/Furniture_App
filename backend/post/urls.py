from django.urls import path, include
from .views import LatestPostsList,AddPosts
from post import views
urlpatterns = [
    path('latest-posts/', views.LatestPostsList.as_view()), #zwraca ostatnio dodane posty
    path('add-post/', views.AddPosts.as_view()), #dodawanie nowych postów

]