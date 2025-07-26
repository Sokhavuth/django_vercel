from django.db import models
import uuid
from django.utils import timezone

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    thumb = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    date = models.CharField(max_length=255)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    categories = models.CharField(max_length=255)
    thumb = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    videos = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    expiration = models.DateTimeField(null=True, blank=True)

