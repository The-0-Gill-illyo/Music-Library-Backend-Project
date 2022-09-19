from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_list),
    path('<int:pk>/', views.song_details),
    path('like/<int:pk>/', views.liked_song),
    path('dislike/<int:pk>/', views.disliked_song),
]