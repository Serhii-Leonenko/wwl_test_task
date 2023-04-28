from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True, )
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ["-creation_date"]
