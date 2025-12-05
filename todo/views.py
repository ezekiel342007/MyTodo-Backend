from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TaskModel, TrackModel
from .serializers import (CreateTaskSerializer, CreateTrackSerializer,
                          TaskSerializer, TrackSerializer)

# Create your views here.


class CreateTrack(generics.CreateAPIView):
    serializer_class = CreateTrackSerializer
    queryset = TrackModel.objects.all()  # pyright: ignore[reportAttributeAccessIssue]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["owner"] = self.request.user
        return context


class SingleTrack(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrackSerializer
    queryset = TrackModel.objects.all()  # pyright: ignore[reportAttributeAccessIssue]
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]


class Tracks(generics.ListAPIView):
    serializer_class = TrackSerializer
    queryset = TrackModel.objects.all()  # pyright: ignore[reportAttributeAccessIssue]
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]


class CreateTasks(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateTaskSerializer

    def get_queryset(self):
        track_id = self.kwargs.get("pk")
        try:
            track = (
                TrackModel.objects.get(  # pyright: ignore[reportAttributeAccessIssue]
                    id=track_id, owner=self.request.user
                )
            )
        except TrackModel.DoesNotExist:  # pyright: ignore[reportAttributeAccessIssue]
            raise NotFound(
                "Track not found or you do not have permission to acccess it"
            )

        return TaskModel.objects.filter(  # pyright: ignore[reportAttributeAccessIssue]
            track=track
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        track_id = self.kwargs.get("pk")
        try:
            track_instance = (
                TrackModel.objects.get(  # pyright: ignore[reportAttributeAccessIssue]
                    id=track_id, owner=self.request.user
                )
            )
            context["track_instance"] = track_instance
        except TrackModel.DoesNotExist:  # pyright: ignore[reportAttributeAccessIssue]
            raise NotFound(
                "Track not found or you do not have permission to acccess it"
            )

        return context


class ListTasks(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        track_id = self.kwargs.get("pk")
        try:
            track = (
                TrackModel.objects.get(  # pyright: ignore[reportAttributeAccessIssue]
                    id=track_id, owner=self.request.user
                )
            )
        except TrackModel.DoesNotExist:  # pyright: ignore[reportAttributeAccessIssue]
            raise NotFound(
                "Track not found or you do not have permission to acccess it"
            )

        return TaskModel.objects.filter(  # pyright: ignore[reportAttributeAccessIssue]
            track=track
        )


class SingleTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    lookup_field = "id"

    def get_queryset(self):
        track_id = self.kwargs.get("pk")
        try:
            track = (
                TrackModel.objects.get(  # pyright: ignore[reportAttributeAccessIssue]
                    id=track_id, owner=self.request.user
                )
            )
        except TrackModel.DoesNotExist:  # pyright: ignore[reportAttributeAccessIssue]
            raise NotFound(
                "Track not found or you do not have permission to acccess it"
            )

        return TaskModel.objects.filter(  # pyright: ignore[reportAttributeAccessIssue]
            track=track
        )
