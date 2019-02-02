from datetime import datetime
from django.db import models

class Mes(models.Model):
    """
    Model for storing messages
    """
    id: int = models.PositiveIntegerField(primary_key=True, default=0)
    name: str = models.TextField(default="Bot")
    content: str = models.TextField(default="Bla bla bla")
    updated_at: datetime = models.DateTimeField()
    created_at: datetime = models.DateTimeField()
