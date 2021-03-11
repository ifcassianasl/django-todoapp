from django.db import models
import uuid

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=80)
    color = models.CharField(max_length=7, default="#ffffff")

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    content = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.content
