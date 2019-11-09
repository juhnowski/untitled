from django.db import models


# Create your models here.
class Request(models.Model):
    """
    Class or user's serch requests
    """
    text = models.CharField(
        max_length=250,
        unique=False,
    )
