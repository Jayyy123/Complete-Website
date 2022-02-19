from django.db import models
import uuid

class Todoform(models.Model):

    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length=200, blank =True, null=True)
    due_date = models.DateField(blank=True,null=True)
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self) -> str:
        return self.title


