from rest_framework import serializers

from users.models import CustomUser
from users.serializers import CustomUserSerializer

from .models import TaskModel, TrackModel


class CreateTrackSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = TrackModel
        fields = ["id", "name", "owner"]
        read_only_fields = ["id", "owner"]

    def create(self, validated_data) -> TrackModel:
        owner = self.context.get("request").user
        track = (
            TrackModel.objects.create(  # pyright: ignore[reportAttributeAccessIssue]
                owner=owner, **validated_data
            )
        )
        return track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackModel
        fields = "__all__"


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ["title", "date", "category", "important"]

    def create(self, validated_data) -> TaskModel:
        task = TaskModel.objects.create(  # pyright: ignore[reportAttributeAccessIssue]
            **validated_data
        )
        return task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ["all"]
