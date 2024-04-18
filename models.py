from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    confluence_version = models.CharField(max_length=20)
    golden_image_version = models.CharField(max_length=20)
