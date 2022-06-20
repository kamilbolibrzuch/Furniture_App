from django.urls import path, include
from .views import LatestPostsList
from post import views
urlpatterns = [
    path('latest-posts/', views.LatestPostsList.as_view()),

]