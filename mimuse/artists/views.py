from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.urls import reverse_lazy
from .models import Artist
from django.contrib import messages
from django.db.models import Q
# Create your views here.



class ArtistListView(ListView):
    context_object_name = 'artists'
    model = Artist
    template_name = 'artists/artist_list.html'

class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist_details'
    template_name = 'artists/artist_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        artist = Artist.objects.get(id=self.get_object().id)
        context['songs'] = artist.songs.all()
        context['albums'] = artist.albums.all()
        context['exist'] = artist.albums.all().exists()
        return context

class SearchResultsListView(ListView):
    model = Artist
    context_object_name = 'artist_list'
    template_name = 'artists/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Artist.objects.filter(
            Q(name__icontains = query) | Q(name__icontains = query) )
