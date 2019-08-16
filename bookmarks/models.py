from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BookMark(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    lat = models.CharField(max_length=120)
    lon = models.CharField(max_length=120)
