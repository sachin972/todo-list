from django.db import models

# Create your models here.
class Lists(models.Model):
    todo = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    progress = models.CharField(max_length=10)
    comments = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.todo}: {self.description}. {self.progress}. {self.comments}."