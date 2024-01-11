from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
# from django.contrib import messages
from .models import Album, Song
# Create your views here.

class SongListView(ListView):
    model = Song
    
class AlbumListView(ListView):
    model = Album
    
# class ArtistDetailView(DetailView):
#     model = Artist
