from django.urls import path

from . import views

app_name = "artists"

urlpatterns = [
    path('', views.ArtistListView.as_view(), name="artist_list"),
    path("<int:pk>", views.ArtistDetailView.as_view(), name="artist_detail")
]