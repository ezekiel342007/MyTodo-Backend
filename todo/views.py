from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TaskModel, TrackModel
from .serializers import CreateTrackSerializer, TaskSerializer, TrackSerializer

# Create your views here.


class Tracks(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrackSerializer
    queryset = TrackModel.objects.all()
    lookup_field = "pk"
    # permission_classes = [IsAuthenticated]


class TrackTasks(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request: Request, pk: str) -> Response:
        tasks = TaskModel.objects.filter(track__id=pk)
        serializer = CreateTrackSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, pk: str) -> Response:
        serializer = CreateTrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
