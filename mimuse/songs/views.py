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

class FavoritesListView(ListView):
    model = Song
    
class SearchAlbumsListView(ListView):
    model = Album
    context_object_name = 'album_list'
    template_name = 'songs/album_search.html'

    def get_queryset(self):
        query = self.request.GET.get('qa')
        response = Album.objects.filter(
            Q(title__icontains = query) | Q(title__icontains = query) )
        if response.exists():
            return response
        else:
            messages.add_message(
            self.request, messages.SUCCESS,
            'No such album found in the database')
            return response
        
class SearchSongsListView(ListView):
    model = Song
    context_object_name = 'song_list'
    template_name = 'songs/song_search.html'

    def get_queryset(self):
        query = self.request.GET.get('qs')
        response = Song.objects.filter(
            Q(title__icontains = query) | Q(title__icontains = query) )
        if response.exists():
            return response
        else:
            messages.add_message(
            self.request, messages.SUCCESS,
            'No such song found in the database')
            return response