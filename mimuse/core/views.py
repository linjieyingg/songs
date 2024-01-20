from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from songs.models import Song
from artists.models import Artist
from django.views.generic import ListView
from django.shortcuts import get_object_or_404


# Create your views here.


def main(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

class RecommendedListView(ListView):
    model = Song
    context_object_name = 'songs_list'
    template_name = 'core/home.html'
    def get_queryset(self):
        response = Song.objects.filter(recommended=True)
        return response