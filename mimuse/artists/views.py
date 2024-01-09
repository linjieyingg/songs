from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
# from django.contrib import messages
from .models import Artist
# Create your views here.

class ArtistListView(ListView):
    model = Artist
    
class ArtistDetailView(DetailView):
    model = Artist
    