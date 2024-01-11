from django.urls import path

from . import views

app_name = "songs"

urlpatterns = [
    path('', views.SongListView.as_view(), name="song_list"),
    path('albums/', views.AlbumListView.as_view(), name="album_list"),
    # path("<int:pk>", views.ArtistDetailView.as_view(), name="artist_detail")
]