from django.db import models
from .SingletonModel import SingletonModel

# Create your models here.
class History(SingletonModel):
    history = models.TextField(default="[]")


