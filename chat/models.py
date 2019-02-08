from datetime import datetime
from django.db import models

class Mes(models.Model):
    """
    Model for storing messages
    """
    id= models.PositiveIntegerField(primary_key=True, default=0)
    name= models.TextField(default="Bot")
    content= models.TextField(default="Bla bla bla")
    updated_at= models.DateTimeField()
    created_at= models.DateTimeField()
