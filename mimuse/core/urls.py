from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
   path("", views.RecommendedListView.as_view(template_name='core/home.html'), name="main"),
]