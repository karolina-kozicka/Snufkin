import random
import factory
from django.contrib.gis.geos import Point

from . import models
from snufkin.users.factories import UserFactory


class PlaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Place

    name = factory.Sequence(lambda n: "Place {n}")
    point = factory.LazyFunction(
        lambda: Point(random.uniform(-180, 180), random.uniform(-90, 90))
    )
    user = factory.SubFactory(UserFactory)
