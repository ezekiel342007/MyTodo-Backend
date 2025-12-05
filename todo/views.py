from rest_framework import generics, status
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


class Tasks(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request: Request, pk: str) -> Response:
        tasks = TaskModel.objects.filter(  # pyright: ignore[reportAttributeAccessIssue]
            track__id=pk
        )  # pyright: ignore[reportAttributeAccessIssue]
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, pk: str) -> Response:
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

