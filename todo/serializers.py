from rest_framework import serializers

from users.serializers import CustomUserSerializer

from .models import TaskModel, TrackModel


class CreateTrackSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = TrackModel
        fields = ["id", "name", "owner"]
        read_only_fields = ["id", "owner"]

    def create(self, validated_data) -> TrackModel:
        owner = self.context.get("owner")
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
        fields = ["id", "title", "date", "category", "important"]
        read_only_fields = ["id"]

    def create(self, validated_data) -> TaskModel:
        track_instance = self.context.get("track_instance")
        task = TaskModel.objects.create(  # pyright: ignore[reportAttributeAccessIssue]
            track=track_instance, **validated_data
        )
        return task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"
