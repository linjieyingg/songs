from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
# from django.contrib import messages
from .models import Artist
from songs.models import Song, Album
# Create your views here.

class ArtistListView(ListView):
    model = Artist
    
class ArtistDetailView(DetailView):
    model = Artist

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        artist = Artist.objects.get(id=self.get_object().id)
        context['songs'] = artist.songs.all()
        context['albums'] = artist.albums.all()

        return context
