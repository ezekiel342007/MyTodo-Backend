from django.urls import path

from .views import Tracks, TrackTasks

urlpatterns = [
    path("tracks/", view=Tracks.as_view()),
    path("tracks/<str:pk>", view=Tracks.as_view()),
    path("tracks/<str:pk>/tasks", view=TrackTasks.as_view()),
]
