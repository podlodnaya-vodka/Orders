from django.core.serializers import json
from django.db import models
import datetime

class Order(models.Model):
    git = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    dateb = models.DateField(default=datetime.date.today)
    datef = models.DateField(default=datetime.date.today)
    correct = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)

