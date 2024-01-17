from django.urls import path

from . import views

app_name = "songs"

urlpatterns = [
    path('', views.SongListView.as_view(template_name='songs/song_list.html'), name="song_list"),
    path('<int:pk>', views.SongDetailView.as_view(), name="song_detail"),
    path('song_search',  views.SearchSongsListView.as_view(template_name='songs/song_search.html'), name="song_search"),
    path('albums/', views.AlbumListView.as_view(), name="album_list"),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name="album_detail"),
    path('favorites/', views.FavoritesListView.as_view(template_name='songs/favorites_list.html'), name="favorites_list"),
    path('favorites/update/<int:pk>/', views.change_favorite, name="update_favorites"),
    path('albums/album_search',  views.SearchAlbumsListView.as_view(), name="album_search"),
]