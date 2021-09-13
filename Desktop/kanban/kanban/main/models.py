from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lists = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title