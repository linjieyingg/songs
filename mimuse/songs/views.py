from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
from django.contrib import messages
from artists.models import Artist
from .models import Album, Song
# Create your views here.

class SongListView(ListView):
    model = Song

class SongDetailView(DetailView):
    model = Song
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        artist = Artist.songs.through.objects.get(song_id=self.get_object().id)
        context['artists'] = Artist.objects.get(id=artist.artist_id)
        return context
    
class AlbumListView(ListView):
    model = Album
    
class AlbumDetailView(DetailView):
    model = Album
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['songs'] = Song.objects.filter(album_id=self.get_object())
        # context["artists"] = Artist.objects.all()
        return context

def ChangeFavorite(request):
    id = request.GET['api_id']
    song = Song.objects.get(api_id=id)
    if (song.favorite == False): song.favorite = True
    else: song.favorie = False
    song.save()
    messages.success(request, "Favorites updated.")
    


class AlbumSongDetailListView(ListView):
    template_name = 'albums_detail.html'
    context_object_name = 'songs_list'
    def get_queryset(self):
        return Song.objects.all()
    
class FavoritesListView(ListView):
    model = Song