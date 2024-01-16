from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from songs.models import Song

# Create your views here.


def main(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

class SongListView(ListView):
    model = Song
    context_object_name = 'songs'
    template_name = 'base.html'
    
    def get_queryset(self):
        response = Song.objects.filter(recommended=True)
        return response