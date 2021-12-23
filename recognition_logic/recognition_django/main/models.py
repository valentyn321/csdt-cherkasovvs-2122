from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255)
    face_location = models.CharField(max_length=255)
    output_location = models.CharField(max_length=255)
