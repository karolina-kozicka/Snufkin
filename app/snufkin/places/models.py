from django.db import models
from django.contrib.gis.db import models as geo_models


class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    point = geo_models.PointField(srid=4326)
    user = models.ForeignKey("users.User", related_name="places", on_delete=models.CASCADE,)