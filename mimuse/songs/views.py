from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
from django.contrib import messages
from .models import Album, Song
# Create your views here.

class SongListView(ListView):
    model = Song

class SongDetailView(DetailView):
    model = Song
    
    
class AlbumListView(ListView):
    model = Album
    
class AlbumDetailView(DetailView):
    model = Album
    
def ChangeFavorite(request):
    id = request.GET['api_id']
    song = Song.objects.get(api_id=id)
    if (song.favorite == False): song.favorite = True
    else: song.favorie = False
    song.save()
    messages.success(request, "Favorites updated.")

class FavoritesListView(ListView):
    model = Song