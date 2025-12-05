from django.urls import path

from .views import CreateTrack, SingleTrack, Tracks

urlpatterns = [
    path("tracks/create/", view=CreateTrack.as_view(), name="create-track"),
    path("tracks/", view=Tracks.as_view(), name="access-tracks"),
    path("tracks/<str:pk>/", view=SingleTrack.as_view(), name="access-tracks"),
]
