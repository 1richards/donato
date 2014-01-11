from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=200)

class Stop(models.Model):
    name = models.CharField(max_length=200)
