from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
from django.contrib import messages
from artists.models import Artist
from .models import Album, Song
from django.db.models import Q
# Create your views here.

class SongListView(ListView):
    model = Song
    context_object_name = 'songs'
    template_name = 'songs/song_list.html'

class SongDetailView(DetailView):
    model = Song
    context_object_name = 'song_details'
    template_name = 'songs/song_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        artist = Artist.songs.through.objects.get(song_id=self.get_object().id)
        context['artists'] = Artist.objects.get(id=artist.artist_id)
        return context
    
class AlbumListView(ListView):
    model = Album
    context_object_name = 'albums'
    template_name = 'songs/album_list.html'
    
class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album_details'
    template_name = 'songs/album_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        artist = Artist.albums.through.objects.get(album_id=self.get_object().id)
        context['artists'] = Artist.objects.get(id=artist.artist_id)
        context['songs'] = Song.objects.filter(album_id=self.get_object())
        return context

def ChangeFavorite(request):
    id = request.GET['api_id']
    song = Song.objects.get(api_id=id)
    if (song.favorite == False): song.favorite = True
    else: song.favorie = False
    song.save()
    messages.success(request, "Favorites updated.")
 
class FavoritesListView(ListView):
    model = Song
    
class SearchAlbumsListView(ListView):
    model = Album
    context_object_name = 'album_list'
    template_name = 'songs/album_search.html'

    def get_queryset(self):
        query = self.request.GET.get('qa')
        return Album.objects.filter(
            Q(title__icontains = query) | Q(title__icontains = query) )
        
class SearchSongsListView(ListView):
    model = Song
    context_object_name = 'song_list'
    template_name = 'songs/song_search.html'

    def get_queryset(self):
        query = self.request.GET.get('qs')
        return Song.objects.filter(
            Q(title__icontains = query) | Q(title__icontains = query) )