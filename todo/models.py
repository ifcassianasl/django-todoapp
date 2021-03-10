from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80)
    todo_text = models.CharField(max_length=250)
    color = models.CharField(max_length=7)