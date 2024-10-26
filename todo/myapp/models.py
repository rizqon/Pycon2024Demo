from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)