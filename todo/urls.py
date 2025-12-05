from django.urls import path

from .views import (CreateTasks, CreateTrack, ListTasks, SingleTask,
                    SingleTrack, Tracks)

urlpatterns = [
    path("tracks/create/", view=CreateTrack.as_view(), name="create-track"),
    path("tracks/", view=Tracks.as_view(), name="access-tracks"),
    path("tracks/<str:pk>/", view=SingleTrack.as_view(), name="access-tracks"),
    path("tracks/<str:pk>/tasks/", view=ListTasks.as_view(), name="list-tasks"),
    path(
        "tracks/<str:pk>/tasks/<str:id>/",
        view=SingleTask.as_view(),
        name="single-task",
    ),
    path(
        "tracks/<str:pk>/tasks/create/", view=CreateTasks.as_view(), name="create-tasks"
    ),
]
