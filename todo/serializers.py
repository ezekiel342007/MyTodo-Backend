from rest_framework import serializers

from .models import TaskModel, TrackModel


class CreateTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackModel
        fields = ["name"]

    def create(self, validated_data) -> TrackModel:
        track = (
            TrackModel.objects.create(  # pyright: ignore[reportAttributeAccessIssue]
                **validated_data
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
