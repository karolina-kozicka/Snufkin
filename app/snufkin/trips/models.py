from django.db import models


class Trip(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    user = models.ForeignKey(
        "users.User", related_name="trips", on_delete=models.CASCADE,
    )
    place = models.ManyToManyField("places.Place", related_name="trips")

    class Meta:
        unique_together = ["name", "user"]

    def __str__(self):
        return self.name
