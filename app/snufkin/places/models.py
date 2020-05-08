from django.db import models
from django.contrib.gis.db import models as geo_models


class Place(models.Model):
    name = models.CharField(max_length=255)
    point = geo_models.PointField(srid=4326)
    user = models.ForeignKey(
        "users.User", related_name="places", on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ["name", "user"]

    def __str__(self):
        return self.name
