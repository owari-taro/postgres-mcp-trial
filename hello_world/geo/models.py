# from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class FeatureMetaData(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    attributes_schema = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source=models.CharField(max_length=255, null=True, blank=True)


class Feature(models.Model):
    geom = models.GeometryField()
    attributes = models.JSONField(null=True, blank=True)
    metadata = models.ForeignKey(
        FeatureMetaData, on_delete=models.CASCADE, related_name="features"
    )
