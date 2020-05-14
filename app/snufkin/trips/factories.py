import datetime
import factory

from . import models
from snufkin.users.factories import UserFactory


class TripFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Trip

    name = factory.Sequence(lambda n: "Trip {n}")
    description = factory.Sequence(lambda n: "Trip description {n}")
    start_date = datetime.date.today() - datetime.timedelta(day=10)
    end_date = datetime.date.today() - datetime.timedelta(day=1)
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def places(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for place in extracted:
                self.places.add(place)
