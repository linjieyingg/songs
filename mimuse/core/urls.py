from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
   path("", views.SongListView.as_view(), name="main"),
]