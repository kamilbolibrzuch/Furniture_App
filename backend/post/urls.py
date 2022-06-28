from django.urls import path, include
from .views import LatestPostsList,PostsListView,PostDetail
from post import views
urlpatterns = [
    path('latest-posts/', views.LatestPostsList.as_view()), #GET zwraca ostatnio dodane posty
    path('add-post/', views.PostsListView.as_view()), #* POST dodawanie nowych postów
    path('add-post/image/', views.PostImagesListView.as_view()), #* POST dodawanie zdjeć do postu
    path('post/<slug:post_slug>/', views.PostDetail.as_view()), #GET pobieranie szczęgółów posta

]