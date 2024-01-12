from django.urls import path

from . import views

app_name = "songs"

urlpatterns = [
    path('', views.SongListView.as_view(), name="song_list"),
    path("<int:pk>", views.SongDetailView.as_view(), name="song_detail"),
    path('albums/', views.AlbumListView.as_view(), name="album_list"),
    path("<int:pk>", views.AlbumDetailView.as_view(), name="album_detail"),
    path('favorites/', views.FavoritesListView.as_view(), name="favorites_list"),
]