from uuid import uuid4

from django.db import models

from users.models import CustomUser

# Create your models here.


class TrackModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class TaskModel(models.Model):
    class CategoryOptions(models.TextChoices):
        HOME = "Home"
        WORK = "Work"
        FUN = "Fun"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    date = models.DateField()
    category = models.CharField(
        max_length=4, choices=CategoryOptions.choices, default=CategoryOptions.WORK
    )
    important = models.BooleanField(
        default=False  # pyright: ignore[reportArgumentType]
    )
    track = models.ForeignKey(
        TrackModel, on_delete=models.CASCADE, related_name="tasks"
    )
